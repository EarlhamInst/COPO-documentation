# Minimal makefile for Sphinx documentation
#
# To build the public documentation, run: $ make html
# To build the internal documentation, run: $ make htmlinternal

# Automatically build the public documentation, run: $ make htmllive
# Automatically build the internal documentation, run: $ make htmlinternallive

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXAUTOBUILD = sphinx-autobuild
SPHINXPROJ    = copo-docs
SOURCEDIR     = .
BUILDDIR      = _build
INTERNALBUILDDIR = _buildinternal
PORT          = 8002

# Log directory
LOGDIR        = $(SOURCEDIR)/logs
DOC8LOG       = $(LOGDIR)/doc8.log
LINKCHECKLOG  = $(LOGDIR)/link_check.log
RSTCHECKLOG   = $(LOGDIR)/rst_check.log
SPELLINGLOG   = $(LOGDIR)/spelling_check.log

# Ignore directives, roles and paths
RSTCHECK_IGNORED_DIRECTIVES = toctree,glossary,collapse,figure,autoclass,currentmodule,seealso,grid,tab-set,youtube
RSTCHECK_IGNORED_ROLES = abbr,email,term,ref

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Command to make internal docs
htmlinternal:
	@echo "Building internal docs"
	@mkdir -p $(INTERNALBUILDDIR)
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(INTERNALBUILDDIR)" $(SPHINXOPTS) $(O) -t internal

.PHONY: htmlinternal Makefile

# Automatically build (public) docs
# e.g. htmllive: checks to run checks before live building
htmllive:
	@echo "Automatically building docs"
	@mkdir -p $(BUILDDIR)
	@# Check if port is in use and kill the process if so
	@if lsof -i TCP:$(PORT) | grep LISTEN >/dev/null 2>&1; then \
		PID=$$(lsof -ti TCP:$(PORT)); \
		echo "Port $(PORT) is in use by PID $$PID. Killing it..."; \
		kill -9 $$PID; \
	fi
	@$(SPHINXAUTOBUILD) --port=$(PORT) --open-browser "$(SOURCEDIR)"/ "$(BUILDDIR)"
	@echo
	@echo "The HTML pages are in $(BUILDDIR)/html."

.PHONY: htmllive Makefile

# Lint, spelling and link checks
# '-@' means continue on errors
checks:
	@echo "Starting documentation checks..."
	@mkdir -p $(LOGDIR)
	@echo "Checking reStructuredText syntax with rstcheck..."
	-@rstcheck --ignore-directives=$(RSTCHECK_IGNORED_DIRECTIVES) \
	    --ignore-roles=$(RSTCHECK_IGNORED_ROLES) \
	    $(shell find $(SOURCEDIR) -name '*.rst') \
	    > $(RSTCHECKLOG) 2>&1 || true
	@echo "Results saved to $(RSTCHECKLOG)"
	@echo
	@echo "Checking .rst files with doc8..."
	-@find $(SOURCEDIR) -name '*.rst'    \
		! -path '$(SOURCEDIR)/$(BUILDDIR)*' \
		! -path '$(SOURCEDIR)/$(INTERNALBUILDDIR)*' \
		! -path '$(SOURCEDIR)/venv*' \
		-print0 | xargs -0 doc8 > $(DOC8LOG) 2>&1
	@echo "Results saved to $(DOC8LOG)"
	@echo
	@echo "Checking grammar and spelling with language_tool_python..."
	@python assets/files/scripts/check_grammar.py
	@echo "Results saved to $(SPELLINGLOG)"
	@echo
	@echo "Checking links with linkcheck..."
	-@sphinx-build -b linkcheck $(SOURCEDIR) $(BUILDDIR)/linkcheck > $(LINKCHECKLOG) 2>&1
	@echo "Results saved to $(LINKCHECKLOG)"
	@echo
	@echo "All checks complete."

.PHONY: checks Makefile

# Automatically build internal docs
htmlinternallive:
	@echo "Automatically building internal docs"
	@mkdir -p $(INTERNALBUILDDIR)
	@$(SPHINXAUTOBUILD) --port=$(PORT) --open-browser "$(SOURCEDIR)"/ "$(INTERNALBUILDDIR)"
	@echo
	@echo "The internal HTML pages are in $(INTERNALBUILDDIR)/html."

.PHONY: htmlinternallive Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)