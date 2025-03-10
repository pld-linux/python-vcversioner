#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Use version control tags to discover version numbers
Summary(pl.UTF-8):	Użycie znaczników kontroli wersji do wykrywania numerów wersji
Name:		python-vcversioner
Version:	2.16.0.0
Release:	10
License:	ISC
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/vcversioner/
Source0:	https://files.pythonhosted.org/packages/source/v/vcversioner/vcversioner-%{version}.tar.gz
# Source0-md5:	aab6ef5e0cf8614a1b1140ed5b7f107d
URL:		https://github.com/habnabit/vcversioner
BuildRequires:	rpm-pythonprov
# for the py_build, py_install macros
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows you to write a setup.py with no version information
specified, and vcversioner will find a recent, properly-formatted VCS
tag and extract a version from it.

%description -l pl.UTF-8
Ten moduł pozwala na tworzenie plików setup.py nie zawierających
informacji o wersji; vcversioner znajdzie najnowszy, właściwie
sformatowany znacznik VCS i wydobędzie z niego numer wersji.

%package -n python3-vcversioner
Summary:	Use version control tags to discover version numbers
Summary(pl.UTF-8):	Użycie znaczników kontroli wersji do wykrywania numerów wersji
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-vcversioner
This module allows you to write a setup.py with no version information
specified, and vcversioner will find a recent, properly-formatted VCS
tag and extract a version from it.

%description -n python3-vcversioner -l pl.UTF-8
Ten moduł pozwala na tworzenie plików setup.py nie zawierających
informacji o wersji; vcversioner znajdzie najnowszy, właściwie
sformatowany znacznik VCS i wydobędzie z niego numer wersji.

%prep
%setup -q -n vcversioner-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/vcversioner.py[co]
%{py_sitescriptdir}/vcversioner-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-vcversioner
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/vcversioner.py
%{py3_sitescriptdir}/__pycache__/vcversioner.cpython-*.py[co]
%{py3_sitescriptdir}/vcversioner-%{version}-py*.egg-info
%endif
