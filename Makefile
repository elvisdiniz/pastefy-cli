
# Makefile for pastefy-cli

# --- Configuration ---
CLI_NAME = pastefy-cli
DIST_DIR = dist
BUILD_DIR = build
INSTALL_DIR = $(HOME)/.local/bin

# --- Targets ---

# Default target
all: test build

# Build the single executable
build:
	@echo "Building $(CLI_NAME)..."
	@mkdir -p $(DIST_DIR)
	@pyinstaller main.spec
	@echo "Build complete: $(BIN_DIR)/$(CLI_NAME)"

# Install the executable
install:
	@echo "Installing $(CLI_NAME) to $(INSTALL_DIR)..."
	@mkdir -p $(INSTALL_DIR)
	@cp $(DIST_DIR)/main $(INSTALL_DIR)/$(CLI_NAME)
	@echo "Installation complete."

# Clean up build artifacts
clean:
	@echo "Cleaning up..."
	@rm -rf $(DIST_DIR) $(BUILD_DIR)
	@echo "Clean complete."

# Run tests
test:
	@echo "Running tests..."
	@python3 -m unittest discover tests

.PHONY: all build install clean test
