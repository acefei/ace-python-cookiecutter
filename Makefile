IMAGE_NAME=pycookiecutter
OUTPUT=output/
#CC_CMD=bash
CC_CMD=cookiecutter . --no-input -o $(OUTPUT)

.PHONY: project
project: build-container
	@mkdir -p $(OUTPUT)
	docker run --rm -u $(shell id -u):$(shell id -g) -v $(PWD):/workspace -w /workspace $(IMAGE_NAME):latest $(CC_CMD)

.PHONY: build-container
build-container: Dockerfile
	docker build -t $(IMAGE_NAME) --build-arg UID=$(shell id -u) --build-arg GID=$(shell id -g) $(<D)

.PHONY: clean
clean:
	rm -rf $(OUTPUT)
