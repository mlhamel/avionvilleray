ifndef message
	message = "Updating web app"
endif

ifndef repos
	repos = mlhamel/avionvilleray
endif

ifndef revision
	tag = latest
endif

.SHELLFLAGS = -e
.PHONY: docker-build
.NOTPARALLEL:

default: build
build: docker-build
commit: docker-commit
push: docker-push
tag: docker-tag
docker-build: do-docker-build
docker-commit: do-docker-commit
docker-push: do-docker-push
docker-tag: do-docker-tag
dump1090: do-dump1090

do-docker-build:
	docker build -t avionvilleray --no-cache --rm . | tee build.log || exit 1

do-docker-commit:
	docker commit -m $(message) $(revision) $(repos)

do-docker-push:
	docker push $(repos):$(tag)

do-docker-tag:
	docker tag -f $(revision) $(repos)

do-dump1090:
	cd modules/dump1090 && make clean && make; cd ../../

# Version Bump using bumpversion
patch:
	bumpversion patch
major:
	bumpversion major
minor:
	bumpversion minor

run:
	pserve development.ini
