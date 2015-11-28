
%define	module	shm

Summary:	Python's Shared Memory Module
Summary(pl.UTF-8):	Moduł Pythona do obsługi pamięci dzielonej
Name:		python-%{module}
Version:	1.2.2
Release:	4
License:	GPL
Group:		Libraries/Python
Source0:	http://nikitathespider.com/python/shm/%{module}-%{version}.tar.gz
# Source0-md5:	da6f51301262605c99c3813019831c50
URL:		http://nikitathespider.com/python/shm/
BuildRequires:	python-devel >= 2.2.1
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides an object interface to System V shared memory
IPC, present in most Unix systems.

%description -l pl.UTF-8
Ten moduł udostępnia obiektowy interfejs do komunikacji między
procesami opartej na pamięci współdzielonej, jaka jest dostępna
w większości systemów uniksowych.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install \
	--install-data %{_datadir} \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/shm.so
%{py_sitedir}/shm_wrapper.*
