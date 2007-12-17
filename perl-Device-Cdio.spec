%define module	Device-Cdio
%define name	perl-%{module}
%define version	0.2.4
%define release %mkrel 5

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Module for CD Input and Control library
License:	GPL
Group:		Development/Perl
Source:		%{module}-v%{version}.tar.bz2
# Debian patch (Thx)
Patch0: 05_buffer_overflows_in_perliso9660.dpatch
Patch1: 06_module_build.dpatch
Patch2: 02_wrong_function_name.dpatch
Url:		http://search.cpan.org/search?query=Device-Cdio
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
%patch0 -p1 -b .05
%patch1 -p1 -b .06
%patch2 -p1 -b .02

rm -f t/*pod*.t

%build
%__perl Build.PL installdirs=vendor

./Build CFLAGS="%{optflags}" || :
chmod u+w -R .
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
