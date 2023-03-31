Name:		python-pyproject_hooks
Version:	1.0.0
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/p/pyproject_hooks/pyproject_hooks-%{version}.tar.gz
Summary:	Wrappers to call pyproject.toml-based build backend hooks.
URL:		https://pypi.org/project/pyproject_hooks/
License:	MIT
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Wrappers to call pyproject.toml-based build backend hooks.

%prep
%autosetup -p1 -n pyproject_hooks-%{version}

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/pyproject_hooks
%{py_sitedir}/pyproject_hooks-*.*-info
