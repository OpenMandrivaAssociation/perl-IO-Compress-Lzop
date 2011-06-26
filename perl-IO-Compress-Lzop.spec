%define	upstream_name	 IO-Compress-Lzop
%define upstream_version 2.037

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	IO::Compress::Lzop - Write lzop files/buffers
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/IO/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Compress::LZO)
BuildRequires: perl(IO::Compress::Base) >= %{version}

BuildArch: noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides a Perl interface that allows writing lzop compressed
data to files or buffer.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/*/*
%{perl_vendorlib}/*
