#
# Copyright (C) [2020] Futurewei Technologies, Inc.
#
# FORCE-RISCV is licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY OR
# FIT FOR A PARTICULAR PURPOSE.
# See the License for the specific language governing permissions and
# limitations under the License.
#
REGISTER_BUILDER=./register_builder.py
INSTALL_DIR=../../../../riscv/arch_data
INSTALL_DIR_RV32=../../../../riscv/arch_data_rv32

.PHONY: all
all:
	@$(MAKE) make_dir
	@$(MAKE) registers
	@$(MAKE) install
	@$(MAKE) clean

.PHONY: make_dir
make_dir:
	@mkdir -p output

.PHONY: registers
registers: system_registers system_register_choices register_field_choices
	@echo Done

.PHONY: system_registers
system_registers: $(REGISTER_BUILDER)
	@echo 'Building Registers: system registers'
	@$(REGISTER_BUILDER) --system_registers

.PHONY: system_register_choices
system_register_choices: $(REGISTER_BUILDER)
	@echo 'Building Registers: system register choices'
	@$(REGISTER_BUILDER) --system_register_choices

.PHONY: register_field_choices
register_field_choices: $(REGISTER_BUILDER)
	@echo 'Building Registers: register field choices'
	@$(REGISTER_BUILDER) --register_field_choices

.PHONY: install
install:
	@echo 'Building Registers: installing register files'
	@cp -f output/system_registers_rv64.xml $(INSTALL_DIR)/system_registers_rv64.xml
	@cp -f output/system_register_choices_rv64.xml $(INSTALL_DIR)/system_register_choices_rv64.xml
	@cp -f output/register_field_choices_rv64.xml $(INSTALL_DIR)/register_field_choices_rv64.xml
	@cp -f output/system_registers_rv32.xml $(INSTALL_DIR_RV32)/system_registers_rv32.xml
	@cp -f output/system_register_choices_rv32.xml $(INSTALL_DIR_RV32)/system_register_choices_rv32.xml
	@cp -f output/register_field_choices_rv32.xml $(INSTALL_DIR_RV32)/register_field_choices_rv32.xml

.PHONY: clean
clean:
	@echo 'Building Registers: clean'
	@rm -f output/*.xml output/*.txt

