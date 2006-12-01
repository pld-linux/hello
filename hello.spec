Summary:	Hello, world!
Summary(pl):	Witaj ¶wiecie!
Name:		hello
Version:	2.2
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	ftp://ftp.gnu.org/gnu/hello/%{name}-%{version}.tar.gz
# Source0-md5:	d2298e4b0c0a5b6e0746e929a7d0a401
Patch0:		%{name}-info.patch
Patch1:		%{name}-localenames.patch
URL:		http://www.gnu.org/software/hello/hello.html
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	gettext-devel >= 0.16
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The 'hello' command is for printing a greeting message.

%description -l pl
Komenda 'hello' s³u¿y do wy¶wietlania niezobowi±zuj±cego pozdrowienia.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

# de.po for de_DE exists and is up to date, de_DE.po is outdated
rm -f po/de_DE*

%build
%{__gettextize}
%{__aclocal} -I gnulib/m4
%{__autoconf}
%{__automake}
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
