Summary:	Hello, world!
Summary(pl):	Cze¶æ, to ja!
Name:		hello
Version:	2.1.1
Release:	1
License:	GPL
Group:		Applications
Source0:	ftp://ftp.gnu.org/gnu/hello/%{name}-%{version}.tar.gz
Patch0:		%{name}-pl.po-update.patch
URL:		http://www.gnu.org/software/hello/hello.html
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The 'hello' command is for printing a greeting message.

%description -l pl
Komenda 'hello' slu¿y do wy¶wietlania niezobowi±zuj±cego pozdrowienia.

%prep
%setup -q
%patch -p1

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog* NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
%{_infodir}/*.info*
