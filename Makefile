
# Makefile for pastefy-cli

# --- Configuration ---
CLI_NAME = pastefy-cli
DIST_DIR = dist
BIN_DIR = $(DIST_DIR)/bin
INSTALL_DIR = $(HOME)/.local/bin

# --- Targets ---

# Default target
all: test build

# Build the single executable
build:
	@echo "Building $(CLI_NAME)..."
	@mkdir -p $(BIN_DIR)
	@echo '#!/usr/bin/env python' > $(BIN_DIR)/$(CLI_NAME)
	@echo '' >> $(BIN_DIR)/$(CLI_NAME)
	@grep -e "^import" main.py >> $(BIN_DIR)/$(CLI_NAME)
	@cat pastefy_cli.py >> $(BIN_DIR)/$(CLI_NAME)
	@echo '' >> $(BIN_DIR)/$(CLI_NAME)
	@grep -v "from pastefy_cli import" main.py | grep -v -e "^import" | grep -v -e "^\s*#" >> $(BIN_DIR)/$(CLI_NAME)
	@chmod +x $(BIN_DIR)/$(CLI_NAME)
	@echo "Build complete: $(BIN_DIR)/$(CLI_NAME)"

# Install the executable
install: build
	@echo "Installing $(CLI_NAME) to $(INSTALL_DIR)..."
	@mkdir -p $(INSTALL_DIR)
	@cp $(BIN_DIR)/$(CLI_NAME) $(INSTALL_DIR)/
	@echo "Installation complete."

# Clean up build artifacts
clean:
	@echo "Cleaning up..."
	@rm -rf $(DIST_DIR)
	@echo "Clean complete."

# Run tests
test:
	@echo "Running tests..."
	@python3 -m unittest discover tests

.PHONY: all build install clean test
