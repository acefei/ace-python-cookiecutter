IMAGE_NAME=pycookiecutter
OUTPUT=output/
PYPROJ_PATH=$(wildcard $(OUTPUT)/*)
CC_CMD=cookiecutter . --no-input -o $(OUTPUT)

.PHONY: project container clean


project: container
	$(MAKE) -C $(PYPROJ_PATH) init

container: Dockerfile
	@mkdir -p $(OUTPUT)
	docker build -t $(IMAGE_NAME) --build-arg UID=$(shell id -u) --build-arg GID=$(shell id -g) $(<D)
	docker run --rm -u $(shell id -u):$(shell id -g) -v $(PWD):/workspace -w /workspace $(IMAGE_NAME):latest $(CC_CMD)

clean:
	rm -rf $(OUTPUT)
