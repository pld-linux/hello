Summary:	Hello, world!
Summary(pl.UTF-8):	Witaj świecie!
Name:		hello
Version:	2.3
Release:	1
License:	GPL v3+
Group:		Applications
Source0:	http://ftp.gnu.org/gnu/hello/%{name}-%{version}.tar.gz
# Source0-md5:	de3187eac06baf5f0506c06935a1fd29
Patch0:		%{name}-info.patch
Patch1:		%{name}-localenames.patch
Patch2:		%{name}-pl.po-update.patch
URL:		http://www.gnu.org/software/hello/hello.html
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	gettext-devel >= 0.16
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The 'hello' command is for printing a greeting message.

%description -l pl.UTF-8
Komenda 'hello' służy do wyświetlania niezobowiązującego pozdrowienia.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

rm -f po/stamp-po
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

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog* NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
%{_infodir}/*.info*
