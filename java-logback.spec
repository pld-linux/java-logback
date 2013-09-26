%define		srcname		logback
%include	/usr/lib/rpm/macros.java
Summary:	A Java logging library
Name:		java-%{srcname}
Version:	1.0.13
Release:	1
License:	LGPL v2 or EPL
Group:		Libraries/Java
Source0:	http://logback.qos.ch/dist/%{srcname}-%{version}.tar.gz
# Source0-md5:	58e056b06b91d761cb6109a580f9f8ce
URL:		http://logback.qos.ch/
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jpackage-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Logback is intended as a successor to the popular log4j project. At
present time, logback is divided into three modules, logback-core,
logback-classic and logback-access.

The logback-core module lays the groundwork for the other two modules.
The logback-classic module can be assimilated to a significantly
improved version of log4j. Moreover, logback-classic natively
implements the SLF4J API so that you can readily switch back and forth
between logback and other logging frameworks such as log4j or
java.util.logging (JUL).

The logback-access module integrates with Servlet containers, such as
Tomcat and Jetty, to provide HTTP-access log functionality. Note that
you could easily build your own module on top of logback-core.

%package javadoc
Summary:	Javadoc for %{name}
Group:		Documentation

%description javadoc
API documentation for the Logback library

%package access
Summary:	Logback-access module for Servlet integration
Group:		Libraries/Java
Requires:	jpackage-utils

%description access
The logback-access module integrates with Servlet containers, such as
Tomcat and Jetty, to provide HTTP-access log functionality. Note that
you could easily build your own module on top of logback-core.

%package examples
Summary:	Logback Examples Module
Group:		Libraries/Java

%description examples
logback-examples module.

%prep
%setup -q -n %{srcname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}
for jar in core classic access; do
	cp -p %{srcname}-$jar-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}-$jar-%{version}.jar
	ln -s %{srcname}-$jar-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}-$jar.jar
done

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a %{srcname}-examples/src $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.txt
%{_javadir}/logback-classic-%{version}.jar
%{_javadir}/logback-classic.jar
%{_javadir}/logback-core-%{version}.jar
%{_javadir}/logback-core.jar

%files javadoc
%defattr(644,root,root,755)
%doc docs/*

%files access
%defattr(644,root,root,755)
%{_javadir}/logback-access-%{version}.jar
%{_javadir}/logback-access.jar

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
