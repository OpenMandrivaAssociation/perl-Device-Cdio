%define module	Device-Cdio
%define name	perl-%{module}
%define version	0.2.4
%define release %mkrel 4

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Module for CD Input and Control library
License:	GPL
Group:		Development/Perl
Source:		%{module}-v%{version}.tar.bz2
Url:		http://search.cpan.org/module/RPM4
Buildroot:	%{_tmppath}/%{name}-root
BuildRequires: perl-devel >= 5.8.0
BuildRequires: perl(ExtUtils::PkgConfig)
BuildRequires: perl(Module::Build)
BuildRequires: perl-version
BuildRequires: libcdio-devel 
BuildRequires: swig
Requires:	perl

%description
A module to make easier temporary directories deletion

%prep
%setup -q -n %{module}-v%{version}

%build
%__perl Build.PL installdirs=vendor
./Build CFLAGS="%{optflags}"

%check
./Build test

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
./Build install destdir=%{buildroot}

%files
%defattr(-,root,root)
%{perl_vendorarch}/*
%_mandir/*/*

