%define	modname	Params-Validate
%define	modver	1.06

Summary:	Validate method/function call parameters
Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	9
License:	GPLv2+ or Artistic
Group:		Development/Other
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://www.cpan.org/modules/by-module/Params/%{modname}-%{modver}.tar.gz
BuildRequires:	perl(Attribute::Handlers)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Module::Implementation)
BuildRequires:	perl(ExtUtils::CBuilder)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl-devel >= 2:5.14
BuildRequires:	perl-List-MoreUtils >= 0.320.0-3

%description
The Params::Validate module provides a flexible system for validation
method/function call parameters.

The validation can be as simple as checking for the presence of required
parameters or as complex as validating object classes (via isa) or capabilities
(via can), checking parameter types, and using customized callbacks to ensure
data integrity.

%prep
%setup -qn %{modname}-%{modver}

%build
perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc README Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

