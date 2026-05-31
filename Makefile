BENCHMARKOOR_TOKEN := $(shell jq -r .benchmarkoor_bearer_token secrets.json)
export BENCHMARKOOR_TOKEN

.PHONY: all fetch gasfit site clean

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

clean:
	rm -rf data/ docs/
