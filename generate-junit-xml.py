import sys
import xml.etree.ElementTree as ET

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file) as f:
    lines = f.readlines()

total_tests = 0
failures = 0
classname = "HelloTest"

for line in lines:
    if line.strip() == ".":
        total_tests += 1
    elif "FAILURES!!!" in line:
        failures = 1

# XML root
testsuite = ET.Element("testsuite", {
    "name": classname,
    "tests": str(total_tests),
    "failures": str(failures),
    "errors": "0",
    "skipped": "0"
})

# Dummy testcase for now
ET.SubElement(testsuite, "testcase", {
    "classname": classname,
    "name": "testAdd",
    "time": "0.001"
})

# Output XML
tree = ET.ElementTree(testsuite)
tree.write(output_file, encoding="utf-8", xml_declaration=True)
