#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ntlm-auth
Version  : 1.2.0
Release  : 1
URL      : https://github.com/jborean93/ntlm-auth/archive/v1.2.0.tar.gz
Source0  : https://github.com/jborean93/ntlm-auth/archive/v1.2.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: ntlm-auth-python3
Requires: ntlm-auth-license
Requires: ntlm-auth-python
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
ntlm-auth
=========
[![Build Status](https://travis-ci.org/jborean93/ntlm-auth.svg?branch=master)](https://travis-ci.org/jborean93/ntlm-auth)[![Build status](https://ci.appveyor.com/api/projects/status/osvvfgmhfk4anvu0/branch/master?svg=true)](https://ci.appveyor.com/project/jborean93/ntlm-auth/branch/master)[![Coverage Status](https://coveralls.io/repos/github/jborean93/ntlm-auth/badge.svg?branch=master)](https://coveralls.io/github/jborean93/ntlm-auth?branch=master)

%package license
Summary: license components for the ntlm-auth package.
Group: Default

%description license
license components for the ntlm-auth package.


%package python
Summary: python components for the ntlm-auth package.
Group: Default
Requires: ntlm-auth-python3

%description python
python components for the ntlm-auth package.


%package python3
Summary: python3 components for the ntlm-auth package.
Group: Default
Requires: python3-core

%description python3
python3 components for the ntlm-auth package.


%prep
%setup -q -n ntlm-auth-1.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1534370438
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/ntlm-auth
cp LICENSE %{buildroot}/usr/share/doc/ntlm-auth/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/ntlm-auth/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
