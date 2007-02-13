
%define	module	shm

Summary:	Python's Shared Memory Module
Summary(pl.UTF-8):	Moduł Pythona do obsługi pamięci dzielonej
Name:		python-%{module}
Version:	1.0
Release:	4
License:	GPL
Group:		Libraries/Python
# Source0:	http://ftp.psychosis.com/python/%{module}-%{version}.tar.gz
Source0:	http://gigue.peabody.jhu.edu/~mdboom/omi/source/shm_source/shmmodule.c
Source1:	python-shm-setup.py
URL:		http://gigue.peabody.jhu.edu/~mdboom/omi/source/shm_source/shm.html
BuildRequires:	python-devel >= 2.2.1
BuildRequires:	python-modules
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
%setup -q -c -T
install %{SOURCE0} .
install %{SOURCE1} .

%build
python python-shm-setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python python-shm-setup.py install --optimize=2 --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/shm.so
