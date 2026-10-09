# Nokri

A project for collecting job postings from multiple sources and preparing them for later enrichment and use.

## First milestone

Collect job postings from sources such as Greenhouse and Lever, and store the raw responses in Cloudflare R2. Keeping the original responses lets us refine parsing and transformations later without relying on a database schema now.

## Later

Enrich the collected postings and transform them into a database schema once that schema is defined. See [SETUP.md](SETUP.md) for the current local setup; usage instructions will be added as the ingestion pipeline takes shape.
