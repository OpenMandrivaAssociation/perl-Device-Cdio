%define module	Device-Cdio
%define name	perl-%{module}
%define version	0.2.4
%define release %mkrel 12

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Module for CD Input and Control library
License:	GPL
Group:		Development/Perl
URL:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Device/%{module}-v%{version}.tar.bz2
# Debian patch (Thx)
Patch1: 01_invalid_cflags.patch
Patch2: 02_wrong_function_name.patch
Patch3: 03_version_information_in_swig.patch
Patch4: 04_wrong_handling_of_output_parameters.patch
Patch5: 05_buffer_overflows_in_perliso9660.patch
Patch6: 06_module_build.patch
Patch7: 07_pod-coverage.patch
BuildRequires: perl-devel >= 5.8.0
BuildRequires: perl(ExtUtils::PkgConfig)
BuildRequires: perl(Module::Build)
BuildRequires: perl-version
BuildRequires: libcdio-devel 
BuildRequires: swig
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
A module to make easier temporary directories deletion

%prep
%setup -q -n %{module}-v%{version}
%patch1 -p1 -b .01
%patch2 -p1 -b .02
#%patch3 -p1 -b .03
%patch4 -p1 -b .04
%patch5 -p1 -b .05
%patch6 -p1 -b .06
%patch7 -p1 -b .07
chmod u+w -R .

%build
%__perl Build.PL installdirs=vendor
# M::B copy files read-only, forcing to use 
# a two-pass build command
# https://rt.cpan.org/Ticket/Display.html?id=42777
./Build CFLAGS="%{optflags}" || :
chmod u+w -R .
./Build CFLAGS="%{optflags}"

%check
# test suite doesn't pass
# http://rt.cpan.org/Public/Bug/Display.html?id=42779
#./Build test

%clean
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%files
%defattr(-,root,root)
%{perl_vendorarch}/*
%_mandir/*/*
