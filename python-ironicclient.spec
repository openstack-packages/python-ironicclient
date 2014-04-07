%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

Name:		python-ironicclient
Version:	0.1.2
Release:	5%{?dist}
Summary:	Python client for Ironic

License:	ASL 2.0
URL:		https://pypi.python.org/pypi/python-ironicclient
Source0:	http://tarballs.openstack.org/python-ironicclient/python-ironicclient-0.1.2.tar.gz

Patch0001:	0001-ironicclient-Remove-runtime-dependency-on-python-pbr.patch
Patch0002:	0002-ironicclient-Prevent-pbr-dependencies-handling.patch

BuildArch:	noarch

BuildRequires:	python2-devel
BuildRequires:	python-pbr
BuildRequires:	python-setuptools

Requires:	python-prettytable
Requires:	python-keystoneclient
Requires:	python-six
Requires:	python-stevedore
Requires:	python-anyjson
Requires:	python-httplib2
Requires:	python-lxml

%description
A python and command line client library for Ironic.

%prep
%setup -q -n %{name}-%{version}

%patch0001 -p1
%patch0002 -p1

# We provide version like this in order to remove runtime dep on pbr.
sed -i s/REDHATIRONICCLIENTVERSION/%{version}/ ironicclient/__init__.py

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}


%files
%doc LICENSE README.rst
%{_bindir}/*
%{python2_sitelib}/ironicclient*
%{python2_sitelib}/python_ironicclient*


%changelog

* Wed Mar 26 2014 Angus Thomas <athomas@redhat.com> - 0.1.2-5
- Removed instance of macro in Changelog
- Consistent use of tabs in SPEC file

* Thu Feb 27 2014 Angus Thomas <athomas@redhat.com> - 0.1.2-4
- Switched to patches made with git
- Write REDHATIRONICCLIENTVERSION correctly
- Reordered files section

* Thu Feb 27 2014 Angus Thomas <athomas@redhat.com> - 0.1.2-3
- Added macro fix to support building on EL6

* Wed Feb 26 2014 Angus Thomas <athomas@redhat.com> - 0.1.2-2
- Added patches to remove pbr dependency
- Updated the source URL
- Removed deletion of python_ironicclient.egg-info

* Tue Feb 25 2014 Angus Thomas <athomas@redhat.com> - 0.1.2-1
- Initial package.
