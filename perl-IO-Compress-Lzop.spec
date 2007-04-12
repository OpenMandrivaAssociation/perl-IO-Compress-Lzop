%define	module	IO-Compress-Lzop
%define	name	perl-%{module}
%define	version	2.004
%define	release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	IO::Compress::Lzop - Write lzop files/buffers
License:	GPL or Artistic
Group:		Development/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/P/PM/PMQS/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}
BuildRequires: perl(IO::Compress::Base) >= %version
BuildRequires: perl(Compress::LZO)
BuildArch: noarch

%description
This module provides a Perl interface that allows writing lzop compressed
data to files or buffer.

%prep
%setup -q -n %{module}-%{version}

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


