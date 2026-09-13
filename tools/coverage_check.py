# Copyright 2021-2025 Avaiga Private Limited
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.

import argparse
import sys
import xml.etree.ElementTree as ET


def check_total(coverage_file: str, threshold: float) -> None:
    """Check that total coverage is at least the given threshold."""
    try:
        tree = ET.parse(coverage_file)
        root = tree.getroot()
    except FileNotFoundError:
        print(f"Error: Coverage file '{coverage_file}' not found.", file=sys.stderr)
        sys.exit(1)
    except ET.ParseError as e:
        print(f"Error: Failed to parse coverage file '{coverage_file}': {e}", file=sys.stderr)
        sys.exit(1)

    line_rate = root.get("line-rate")
    if line_rate is None:
        print("Error: Could not find 'line-rate' attribute in coverage XML.", file=sys.stderr)
        sys.exit(1)

    try:
        coverage_percentage = float(line_rate) * 100
    except ValueError:
        print(f"Error: Invalid line-rate value: '{line_rate}'", file=sys.stderr)
        sys.exit(1)

    if coverage_percentage < threshold:
        print(
            f"Error: Total coverage is {coverage_percentage:.2f}%, which is below the threshold of {threshold:.2f}%.",
            file=sys.stderr,
        )
        sys.exit(1)

    print(f"Total coverage is {coverage_percentage:.2f}% (threshold: {threshold:.2f}%).")
    sys.exit(0)


def main() -> None:
    parser = argparse.ArgumentParser(description="Coverage validation tool.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    check_total_parser = subparsers.add_parser("check-total", help="Check total coverage against a threshold.")
    check_total_parser.add_argument("--coverage-file", required=True, help="Path to coverage.xml file.")
    check_total_parser.add_argument("--threshold", type=float, required=True, help="Coverage threshold in percentage.")

    args = parser.parse_args()

    if args.command == "check-total":
        check_total(args.coverage_file, args.threshold)


if __name__ == "__main__":
    main()
