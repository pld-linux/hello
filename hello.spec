Summary:	Hello, world!
Summary(pl):	Cze¶æ, to ja!
Name:		hello
Version:	1.3
Release:	1
License:	GPL
Group:		Applications
Group(de):	Applikationen
Group(pl):	Aplikacje
Source0:	ftp://ftp.gnu.org/gnu/hello/%{name}-%{version}.tar.gz
URL:		http://www.gnu.org/software/hello/hello.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The 'hello' command is for printing a greeting message.

%description -l pl
Komenda 'hello' slu¿y do wy¶wietlania niezobowi±zuj±cego pozdrowienia.

%prep
%setup -q

%build
%configure \
	--prefix=%{_datadir} --exec-prefix=%{_prefix}

%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_infodir}}
install hello $RPM_BUILD_ROOT%{_bindir}
install hello.info $RPM_BUILD_ROOT%{_infodir}

gzip -9nf NEWS README ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%attr(644,root,root) %{_infodir}/*
