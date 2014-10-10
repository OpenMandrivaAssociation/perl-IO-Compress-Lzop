%define	upstream_name  IO-Compress-Lzop
%define upstream_version 2.064

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	IO::Compress::Lzop - Write lzop files/buffers
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/IO/IO-Compress-Lzop-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Compress::LZO)
BuildRequires:	perl(IO::Compress::Base) >= %{version}
BuildRequires:	perl(IO::Uncompress::Base) >= %{version}

BuildArch:	noarch

%description
This module provides a Perl interface that allows writing lzop compressed
data to files or buffer.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/*/*
%{perl_vendorlib}/*

%changelog
* Sun Jun 26 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.37.0-1mdv2011.0
+ Revision: 687342
- update to new version 2.037

* Sat May 14 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.35.0-1
+ Revision: 674664
- update to new version 2.035

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 2.33.0-2
+ Revision: 656931
- rebuild for updated spec-helper

* Wed Feb 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.33.0-1
+ Revision: 635189
- update to new version 2.033

* Tue Jul 27 2010 Jérôme Quelin <jquelin@mandriva.org> 2.30.0-1mdv2011.0
+ Revision: 561932
- update to 2.030

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 2.27.0-1mdv2011.0
+ Revision: 552323
- update to 2.027

* Sun Apr 18 2010 Jérôme Quelin <jquelin@mandriva.org> 2.26.0-1mdv2010.1
+ Revision: 536187
- update to 2.026

* Wed Mar 31 2010 Jérôme Quelin <jquelin@mandriva.org> 2.25.0-1mdv2010.1
+ Revision: 530264
- update to 2.025

* Mon Jan 11 2010 Jérôme Quelin <jquelin@mandriva.org> 2.24.0-1mdv2010.1
+ Revision: 489504
- update to 2.024

* Tue Nov 10 2009 Jérôme Quelin <jquelin@mandriva.org> 2.23.0-1mdv2010.1
+ Revision: 464137
- update to 2.023

* Thu Sep 10 2009 Jérôme Quelin <jquelin@mandriva.org> 2.21.0-1mdv2010.0
+ Revision: 437231
- update to 2.021

* Mon Jun 08 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.020-1mdv2010.0
+ Revision: 383972
- update to new version 2.020

* Mon May 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.019-1mdv2010.0
+ Revision: 371955
- new version

* Fri Sep 05 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.015-1mdv2009.0
+ Revision: 281711
- new version

* Thu Jul 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.012-1mdv2009.0
+ Revision: 236719
- update to new version 2.012

* Wed May 21 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.011-1mdv2009.0
+ Revision: 209684
- update to new version 2.011

* Wed May 07 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.010-1mdv2009.0
+ Revision: 202822
- new version

* Wed Apr 23 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.009-1mdv2009.0
+ Revision: 196826
- update to new version 2.009

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Nov 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.008-1mdv2008.1
+ Revision: 108303
- update to new version 2.008

* Mon Sep 03 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.006-1mdv2008.0
+ Revision: 78416
- update to new version 2.006

* Thu Jul 05 2007 Olivier Thauvin <nanardon@mandriva.org> 2.005-1mdv2008.0
+ Revision: 48385
- 2.005


* Mon Mar 05 2007 Olivier Thauvin <nanardon@mandriva.org> 2.004-1mdv2007.0
+ Revision: 132965
- 2.004

* Sun Jan 07 2007 Olivier Thauvin <nanardon@mandriva.org> 2.003-1mdv2007.1
+ Revision: 104993
- first mandriva package
- Create perl-IO-Compress-Lzop



