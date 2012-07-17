Summary: A cron job to run the glue-validator command every hour and store the result in a log file.
Name: glue-validator-cron
Version: 1.0.0
Release: 1%{?dist}
# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
#  svn export http://svnweb.cern.ch/guest/gridinfo/glue-validator-cron/tags/R_%{version}/%{name}-%{version}
#  tar -czvf %{name}-%{version}.tar.gz %{name}-%{version}
Source0: %{name}-%{version}.tar.gz
License: ASL 2.0
Group: System/Monitoring
BuildRoot: %{_tmppath}/%{name}-%{version}-build
BuildArch: noarch
Requires: glue-validator
Url: http://cern.ch/glue

%description
A cron job to run the glue-validator command every hour and store the result in a log file. 

%prep
%setup -q

%build
# Nothing to build

%install
rm -rf %{buildroot}
make install prefix=%{buildroot}

%post%
/etc/cron.hourly/glue-validator-cron

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%dir /var/log/glue-validator/
/etc/cron.hourly/glue-validator-cron


%changelog
* Tue Jul 16 2012 Maria Alandes <maria.alandes.pradillo@cern.ch>  - 1.0.0-1
- Initial Release
