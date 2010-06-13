# Maintainer: <mindbug> John-Patrik Nilsson, themindbug@gmail.com
# Copyright info

"""
	Pseudo code
	
	get pickled stream from pkgcore_check (or wherever), the stream is probably a Reporter-object containing Result-objects

	unpickle the stream

	is there a way to convert objects into SQL? ORM, SQLAlchemy?

	loop through the stream and input the objects into a SQLite3 db

	TODO
		read about for
		and read about try (if the classes miss one attribute)
		get common "fields" for the check-objects
		hint: pkgcore_checks.base.Result
"""
#from pkgcore.config import load_config
#repo_string = '/usr/portage'
#repo = load_config().repo[repo_string]

#file = open('repo.pkl', 'w')
#p = snakeoil.pickling.Pickler(repo, file)
#file.close()

# we want to use this to grab the pickle stream...
from snakeoil.pickling import iter_stream
# open the ready-made binary pickle file, containing 
# pkgcore_checks.base.Result objects, or derivate 
# objects of that class.
pickle_file = open("qa-results.pcheck")
# iter_stream = class generator
# create a list of the contents of the pickled file
# with the help of the generator object iter_stream
check_list = list(iter_stream(pickle_file))
# check_list[0] is a list header!
print check_list[1]
dir(check_list[1])
# repr(checks[6]).split()[0]
