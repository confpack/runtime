.PHONY: prep jinja2 all


WORKDIR=workdir

# Dependencies!
JINJA2_GIT=https://github.com/mitsuhiko/jinja2.git
JINJA2_TAG=2.8

MARKUPSAFE_GIT=https://github.com/mitsuhiko/markupsafe.git
MARKUPSAFE_TAG=0.23

all: jinja2
	rm -rf $(WORKDIR)

prep:
	mkdir -p $(WORKDIR)

# Each dependant library here

jinja2: prep
	rm -rf jinja2
	git clone $(JINJA2_GIT) $(WORKDIR)/jinja2
	cd $(WORKDIR)/jinja2 && git checkout $(JINJA2_TAG)
	cp -R $(WORKDIR)/jinja2/jinja2 .

	rm -rf markupsafe
	git clone $(MARKUPSAFE_GIT) $(WORKDIR)/markupsafe
	cd $(WORKDIR)/markupsafe && git checkout $(MARKUPSAFE_TAG)
	cp -R $(WORKDIR)/markupsafe/markupsafe .

