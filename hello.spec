Summary:     	Hello, world!
Summary(pl): 	Cze¶æ, to ja!
Name:        	hello
Version:     	1.3
Release:     	1
Group:       	Networking/Daemons
Group(pl):   	Sieciowe/Serwery
Copyright:   	GPL
URL:         	ftp://gnu.org/pub/hello/%{name}-%{version}.tar.gz
Source:      	%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The 'hello' command is for printing a greeting message.

%description -l pl
Komenda 'hello' slu¿y do wy¶wietlania niezobowi±zuj±cego pozdrowienia.

%prep

%setup -q

%build
%configure \
	--prefix=/usr/share --exec-prefix=/usr

%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_infodir}
install -s hello $RPM_BUILD_ROOT%{_bindir}
install hello.info $RPM_BUILD_ROOT%{_infodir}

gzip -9nf $RPM_BUILD_ROOT%{_infodir}/* \
	NEWS README ChangeLog

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(644,root,root) %{_infodir}/*

%doc *.gz

%clean
rm -rf $RPM_BUILD_ROOT
