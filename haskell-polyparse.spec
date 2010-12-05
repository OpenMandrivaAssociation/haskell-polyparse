%define module  polyparse

Name: haskell-%{module}
Version: 1.3
Release: %mkrel 2
Summary: A variety of alternative parser combinator libraries
Group: Development/Other
License: LGPL
Url: http://www.cs.york.ac.uk/fp/polyparse/
Source: http://hackage.haskell.org/packages/archive/%{module}/%{version}/%{module}-%{version}.tar.gz
BuildRoot: %_tmppath/%name-%version-%release-root
BuildRequires: ghc
BuildRequires: haddock
BuildRequires: haskell-macros

%description
A variety of alternative parser combinator libraries, including the original
HuttonMeijer set. The Poly sets have features like good error reporting,
arbitrary token type, running state, lazy parsing, and so on. Finally,
Text.Parse is a proposed replacement for the standard Read class, for better
deserialisation of Haskell values from Strings.

%prep
%setup -q -n %{module}-%{version}

%build
%_cabal_build

%_cabal_genscripts

%check
%_cabal_check

%install
%_cabal_install

rm -fr %{buildroot}/%_datadir/*/doc/

%_cabal_rpm_gen_deps

%_cabal_scriptlets

%files
%defattr(-,root,root)
%_docdir/%{module}-%{version}
%_libdir/*
%_cabal_rpm_files

%clean
rm -fr %buildroot


