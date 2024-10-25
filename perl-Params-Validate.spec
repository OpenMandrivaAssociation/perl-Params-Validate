%define	modname	Params-Validate

Summary:	Validate method/function call parameters
Name:		perl-%{modname}
Version:	1.31
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Other
Url:		https://metacpan.org/release/Params-Validate
Source0:	http://www.cpan.org/modules/by-module/Params/%{modname}-%{version}.tar.gz
BuildRequires:	perl(Attribute::Handlers)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Module::Implementation)
BuildRequires:	perl(ExtUtils::CBuilder)
BuildRequires:	perl-devel
BuildRequires:	perl-List-MoreUtils
# For tests
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::Requires)
BuildRequires:	perl(Devel::Peek)

%description
The Params::Validate module provides a flexible system for validation
method/function call parameters.

The validation can be as simple as checking for the presence of required
parameters or as complex as validating object classes (via isa) or capabilities
(via can), checking parameter types, and using customized callbacks to ensure
data integrity.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc Changes
%{perl_vendorarch}/*
%{_mandir}/man3/*
