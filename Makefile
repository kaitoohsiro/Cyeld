# バージョンは変更した？？変更後にアップロードしよう


build-test:
	twine upload --repository testpypi dist/*

build:
	twine upload --repository pypi dist/*