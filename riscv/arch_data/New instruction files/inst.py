from lxml import etree as ET

## starting and ending tags for the instructions xml files

startRootTag = '''<?xml version="1.0" encoding="UTF-8"?>
<!--
 Copyright (C) [2020] Futurewei Technologies, Inc.

 FORCE-RISCV is licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

 THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER
 EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY OR
 FIT FOR A PARTICULAR PURPOSE.
 See the License for the specific language governing permissions and
 limitations under the License.
-->
<instruction_file>
'''

endRootTag = "</instruction_file>"

## files to store the integer, float, double and quad instruction according to their types

RV32IM = open('riscv_instructions_int32.xml', 'wb+')
RV32IM.write(startRootTag.encode())

RV64IM = open('riscv_instructions_int64.xml', 'wb+')
RV64IM.write(startRootTag.encode())

RVF = open('riscv_instructions_float.xml', 'wb+')
RVF.write(startRootTag.encode())

RVD = open('riscv_instructions_double.xml', 'wb+')
RVD.write(startRootTag.encode())

RVQ = open('riscv_instructions_quad.xml', 'wb+')
RVQ.write(startRootTag.encode())

## reading and processing integer, float, double and quad instructios' file

instructionFile = ET.parse('../riscv_instructions.xml')

instructions = instructionFile.getroot()

for instruction in instructions:
    if instruction.attrib['extension'] == 'RV64I' or instruction.attrib['extension'] == 'RV64M' :
        RV64IM.write(ET.tostring(instruction, pretty_print=True))
    elif instruction.attrib['extension'] == 'RV32I' or instruction.attrib['extension'] == 'RV32M' :
        RV32IM.write(ET.tostring(instruction, pretty_print=True))
    elif instruction.attrib['extension'] == 'RV32F' or instruction.attrib['extension'] == 'RV64F' :
        RVF.write(ET.tostring(instruction, pretty_print=True))
    elif instruction.attrib['extension'] == 'RV32D' or instruction.attrib['extension'] == 'RV64D' :
        RVD.write(ET.tostring(instruction, pretty_print=True))
    elif instruction.attrib['extension'] == 'RV32Q' or instruction.attrib['extension'] == 'RV64Q' :
        RVQ.write(ET.tostring(instruction, pretty_print=True))
        
RV64IM.write(endRootTag.encode())
RV64IM.close()

RV32IM.write(endRootTag.encode())
RV32IM.close()

RVF.write(endRootTag.encode())
RVF.close()

RVD.write(endRootTag.encode())
RVD.close()

RVQ.write(endRootTag.encode())
RVQ.close()

###############################################################

## files to store compressed instruction according to their types

RV32C = open('riscv_instructions_compressed_rv32.xml', 'wb+')
RV32C.write(startRootTag.encode())

RV64C = open('riscv_instructions_compressed_rv64.xml', 'wb+')
RV64C.write(startRootTag.encode())

# reading and processing compressed instructions' file

c_instructionsFile = ET.parse('../c_instructions.xml')
c_instructions = c_instructionsFile.getroot()

for instruction in c_instructions:
    if instruction.attrib['extension'] == 'RV64C':
        RV64C.write(ET.tostring(instruction, pretty_print=True))
    elif instruction.attrib['extension'] == 'RV32C':
        RV32C.write(ET.tostring(instruction, pretty_print=True))


RV32C.write(endRootTag.encode())
RV32C.close()

RV64C.write(endRootTag.encode())
RV64C.close()