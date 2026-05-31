BENCHMARKOOR_TOKEN := $(shell jq -r .benchmarkoor_bearer_token secrets.json)
export BENCHMARKOOR_TOKEN

PORT ?= 8000

.PHONY: all fetch gasfit site serve clean

all:
	$(MAKE) fetch
	$(MAKE) gasfit
	$(MAKE) site

fetch:
	benchmarkoor-fetch run --config fetch.yaml --out data/raw/

gasfit:
	evm-gasfit run --config fit.yaml \
		--runtimes data/raw/runtimes.csv \
		--opcounts data/raw/opcounts.json \
		--out data/gasfit/

site:
	python scripts/build_site.py

serve:
	python -m http.server $(PORT) --directory docs/

clean:
	rm -rf data/ docs/
