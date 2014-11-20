%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

Name:		python-ironicclient
Version:	XXX
Release:	XXX{?dist}
Summary:	Python client for Ironic

License:	ASL 2.0
URL:		https://pypi.python.org/pypi/python-ironicclient
Source0:	http://tarballs.openstack.org/python-ironicclient/python-ironicclient-0.3.1.tar.gz

Patch0001:	0001-ironicclient-Remove-runtime-dependency-on-python-pbr.patch

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
%setup -q -n %{name}-%{upstream_version}

%patch0001 -p1

# We provide version like this in order to remove runtime dep on pbr.
sed -i s/REDHATIRONICCLIENTVERSION/%{version}/ ironicclient/__init__.py

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt tools/{pip,test}-requires

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

* Thu Oct 16 2014 Angus Thomas <athomas@redhat.com> - 0.3.1-1
- Rebased to python-ironicclient-0.3.1

* Tue Oct 07 2014 Dan Prince <dprince@redhat.com> - XXX
- Rebase patches.
- Remove requirements.txt and test-requirements.txt via the RPM spec
  file instead of patch files (this is more robust)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

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
