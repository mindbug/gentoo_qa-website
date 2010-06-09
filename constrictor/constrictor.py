# Maintainer: <mindbug> John-Patrik Nilsson, themindbug@gmail.com
# Copyright info

"""
	Pseudo code
	
	get pickled stream from pkgcore_check (or wherever), the stream is probably a Reporter-object containing Result-objects

	unpickle the stream

	is there a way to convert objects into SQL? ORM, SQLAlchemy?

	loop through the stream and input the objects into a SQLite3 db


"""
from pkgcore.config import load_config
repo_string = '/usr/portage'
repo = load_config().repo[repo_string]

file = open('repo.pkl', 'w')
p = snakeoil.pickling.Pickler(repo, file)
file.close()
