DIRS := $(wildcard hello-from-*)

.PHONY: build $(DIRS)

build: $(DIRS)

$(DIRS):
	@echo "Building plug-in: $@"
	@(cd $@ && make build)

HOST_LANG?="python"
run:
	@(cd "hello-in-$(HOST_LANG)" && make run)

