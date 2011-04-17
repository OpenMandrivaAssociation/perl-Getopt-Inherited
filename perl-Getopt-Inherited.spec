%define upstream_name    Getopt-Inherited
%define upstream_version 1.100860

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Handling inherited command-line options
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Getopt/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class::Accessor::Complex)
BuildRequires: perl(Data::Inherited)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(Pod::Usage)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
By subclassing this mixin class, your program gets the ability to inherit
command-line option specifications. If you have several programs that share
common code and common command-line options you don't want to have to write
the command-line processing code again and again. Using this class you can
abstract command-line options shared by your programs into a superclass
from which your programs then inherit. Additionally, this class defines
certain common command-line options itself.

You can also define defaults for command-line options.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/man3/*
%perl_vendorlib/*


