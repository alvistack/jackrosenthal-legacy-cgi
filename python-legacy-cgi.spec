# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-legacy-cgi
Epoch: 100
Version: 2.6.3
Release: 1%{?dist}
BuildArch: noarch
Summary: Fork of the standard library cgi and cgitb modules
License: Python-2.0
URL: https://github.com/jackrosenthal/legacy-cgi/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-pip

%description
Python CGI This is a fork of the standard library modules cgi and cgitb.
They are slated to be removed from the Python standard library in Python
3.13. The purpose of this fork is to support existing CGI scripts using
these modules.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
pip wheel \
    --no-deps \
    --no-build-isolation \
    --wheel-dir=dist \
    .

%install
pip install \
    --no-deps \
    --ignore-installed \
    --root=%{buildroot} \
    --prefix=%{_prefix} \
    dist/*.whl
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-legacy-cgi
Summary: Fork of the standard library cgi and cgitb modules
Requires: python3
Provides: python3-legacy-cgi = %{epoch}:%{version}-%{release}
Provides: python3dist(legacy-cgi) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-legacy-cgi = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(legacy-cgi) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-legacy-cgi = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(legacy-cgi) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-legacy-cgi
Python CGI This is a fork of the standard library modules cgi and cgitb.
They are slated to be removed from the Python standard library in Python
3.13. The purpose of this fork is to support existing CGI scripts using
these modules.

%files -n python%{python3_version_nodots}-legacy-cgi
%license LICENSE
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-legacy-cgi
Summary: Fork of the standard library cgi and cgitb modules
Requires: python3
Provides: python3-legacy-cgi = %{epoch}:%{version}-%{release}
Provides: python3dist(legacy-cgi) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-legacy-cgi = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(legacy-cgi) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-legacy-cgi = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(legacy-cgi) = %{epoch}:%{version}-%{release}

%description -n python3-legacy-cgi
Python CGI This is a fork of the standard library modules cgi and cgitb.
They are slated to be removed from the Python standard library in Python
3.13. The purpose of this fork is to support existing CGI scripts using
these modules.

%files -n python3-legacy-cgi
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-legacy-cgi
Summary: Fork of the standard library cgi and cgitb modules
Requires: python3
Provides: python3-legacy-cgi = %{epoch}:%{version}-%{release}
Provides: python3dist(legacy-cgi) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-legacy-cgi = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(legacy-cgi) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-legacy-cgi = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(legacy-cgi) = %{epoch}:%{version}-%{release}

%description -n python3-legacy-cgi
Python CGI This is a fork of the standard library modules cgi and cgitb.
They are slated to be removed from the Python standard library in Python
3.13. The purpose of this fork is to support existing CGI scripts using
these modules.

%files -n python3-legacy-cgi
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
