%global debug_package %{nil}
#% define _cabal_setup Setup.lhs
#% define _no_haddock 1
%define module polyparse
Name:           haskell-%{module}
Version:        1.8
Release:        1
Summary:        A variety of alternative parser combinator libraries
Group:          Development/Other
License:        LGPL
URL:            http://hackage.haskell.org/package/%{module}
Source0:        http://hackage.haskell.org/packages/archive/%{module}/%{version}/%{module}-%{version}.tar.gz

BuildRequires:  ghc, ghc-devel, haskell-macros, haddock
buildrequires:  haskell(text)
Requires(pre):  ghc
requires(pre):  haskell(text)

%description
A variety of alternative parser combinator libraries, including the original
HuttonMeijer set.  The Poly sets have features like good error reporting,
arbitrary token type, running state, lazy parsing, and so on.  Finally,
Text.Parse is a proposed replacement for the standard Read class, for better
deserialisation of Haskell values from Strings.

%prep
%setup -q -n %{module}-%{version}

%build
%_cabal_build

%install
%_cabal_install
%_cabal_rpm_gen_deps
%_cabal_scriptlets

%check
%_cabal_check

%files
%defattr(-,root,root,-)
%{_docdir}/%{module}-%{version}
%{_libdir}/%{module}-%{version}
%_cabal_rpm_deps_dir
%_cabal_haddoc_files



