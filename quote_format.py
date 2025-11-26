import re

def replace_quote_print_format_value(text, new_value):
    # Replace the numeric value inside any <prefix:QuotePrintFormat>...</prefix:QuotePrintFormat>
    return re.sub(r'<(\w+):QuotePrintFormat>\d+</\1:QuotePrintFormat>',
                  fr'<\1:QuotePrintFormat>{new_value}</\1:QuotePrintFormat>',
                  text)

# Sample input strings
var = """<ims:ContactNode>IBMGB</ims:ContactNode>
<ims:PROFSId>IBMGB</ims:PROFSId>
<ims:ReceiveCopyInd>Y</ims:ReceiveCopyInd>
<ims:QuotePrintFormat>006</ims:QuotePrintFormat>"""

var1 = """<ims:ContactNode>IBMGB</ims:ContactNode>
<ims:PROFSId>IBMGB</ims:PROFSId>
<ims:ReceiveCopyInd>Y</ims:ReceiveCopyInd>
<eql:QuotePrintFormat>006</eql:QuotePrintFormat>"""

var2 = """<ims:ContactNode>IBMGB</ims:ContactNode>
<ims:PROFSId>IBMGB</ims:PROFSId>
<ims:ReceiveCopyInd>Y</ims:ReceiveCopyInd>
<LLPP:QuotePrintFormat>006</LLPP:QuotePrintFormat>"""

# Replace value
new_value = "100"
var = replace_quote_print_format_value(var, new_value)
var1 = replace_quote_print_format_value(var1, new_value)
var2 = replace_quote_print_format_value(var2, new_value)

# Output results
print("Updated var:\n", var)
print("\nUpdated var1:\n", var1)
print("\nUpdated var2:\n", var2)