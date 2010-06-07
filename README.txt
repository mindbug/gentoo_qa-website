====  Last edited  ====
    2010-06-07

====  Project info  ====
    Project Name: Gentoo x86 QA-website
    Project Info: Google Summer of Code 2010 project
    Student Name: John-Patrik Nilsson
    IRC nick: mindbug
    email: themindbug@gmail.com

====  Top-level design  ====
    The project is divided into two parts: 
        A website interface.
            Files: django_gentoo_pkg/*
        A data provider centered around the pkgcore PMS.
            Files: pkgcore_digester/*

====  The website interface  ====
    Read django_gentoo_pkg/README.txt for more info.
    Uses the Django framework.
    Uses AJAX where possible.
    Uses CSS where possible.
    Will provide the best and freshest QA data to developers ever seen.
    Will look stunning and designy.

====  The Python data digester  ====
    Read pkgcore_digester/README.txt for more info.
    Prepares data about ebuild atoms (well, about the entire repository really) from pkgcore, so that the web framework can use this data and present that to the users.
