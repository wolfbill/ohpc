
#
#  Copyright (C) 1994-2016 Altair Engineering, Inc.
#  For more information, contact Altair at www.altair.com.
#   
#  This file is part of the PBS Professional ("PBS Pro") software.
#  
#  Open Source License Information:
#   
#  PBS Pro is free software. You can redistribute it and/or modify it under the
#  terms of the GNU Affero General Public License as published by the Free 
#  Software Foundation, either version 3 of the License, or (at your option) any 
#  later version.
#   
#  PBS Pro is distributed in the hope that it will be useful, but WITHOUT ANY 
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
#  PARTICULAR PURPOSE.  See the GNU Affero General Public License for more details.
#   
#  You should have received a copy of the GNU Affero General Public License along 
#  with this program.  If not, see <http://www.gnu.org/licenses/>.
#   
#  Commercial License Information: 
#  
#  The PBS Pro software is licensed under the terms of the GNU Affero General 
#  Public License agreement ("AGPL"), except where a separate commercial license 
#  agreement for PBS Pro version 14 or later has been executed in writing with Altair.
#   
#  Altair’s dual-license business model allows companies, individuals, and 
#  organizations to create proprietary derivative works of PBS Pro and distribute 
#  them - whether embedded or bundled with other software - under a commercial 
#  license agreement.
#  
#  Use of Altair’s trademarks, including but not limited to "PBS™", 
#  "PBS Professional®", and "PBS Pro™" and Altair’s logos is subject to Altair's 
#  trademark licensing policies.
#

%include %{_sourcedir}/OHPC_macros
%define install_path %{OHPC_PUB}/pbs

%if %{!?PROJ_DELIM:1}%{?PROJ_DELIM:0}
%define PROJ_DELIM -ohpc
%endif

%define _unpackaged_files_terminate_build 0

%define pbs_name pbspro
%define pbs_client client%{PROJ_DELIM}
%define pbs_execution execution%{PROJ_DELIM}
%define pbs_server server%{PROJ_DELIM}
%define pbs_version 13.1.800
%define pbs_release 0
%define pbs_prefix %{install_path}
%define pbs_home /var/spool/pbs
%define pbs_dbuser postgres
%define pbs_dist http://localhost/downloads/%{pbs_name}-%{pbs_version}.tar.gz

Name: %{pbs_name}
Version: %{pbs_version}
Release: %{pbs_release}
Source0: %{pbs_dist}
Source1: OHPC_macros
%if %{defined suse_version}
Source2: pbspro-ohpc-rpmlintrc
%endif
Summary: PBS Professional
License: AGPLv3 with exceptions
URL: http://www.pbspro.com
Vendor: Altair Engineering, Inc.
Prefix: %{pbs_prefix}

%bcond_with alps
%bcond_with cpuset
%bcond_with ibm-ib
%bcond_with ibm-hps

BuildRoot: %{_tmppath}/%{pbs_name}-%{version}-%{release}-root
BuildRequires: gcc
BuildRequires: make
BuildRequires: rpm-build
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: hwloc-devel
BuildRequires: libX11-devel
BuildRequires: libXt-devel
BuildRequires: libedit-devel
BuildRequires: libical-devel
BuildRequires: ncurses-devel
BuildRequires: perl
BuildRequires: postgresql-devel
BuildRequires: python-devel >= 2.6
BuildRequires: python-devel < 3.0
BuildRequires: tcl-devel
BuildRequires: tk-devel
BuildRequires: swig
%if %{defined suse_version}
BuildRequires: libexpat-devel
BuildRequires: libopenssl-devel
BuildRequires: libXext-devel
BuildRequires: libXft-devel
BuildRequires: fontconfig
# FIXME: The SuSE post build checks should not be ignored
BuildRequires: -post-build-checks
%else
BuildRequires: expat-devel
BuildRequires: openssl-devel
BuildRequires: libXext
BuildRequires: libXft
%endif

# Pure python extensions use the 32 bit library path
%{!?py_site_pkg_32: %global py_site_pkg_32 %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(0)")}
%{!?py_site_pkg_64: %global py_site_pkg_64 %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

%description
PBS Professional® is a fast, powerful workload manager and
job scheduler designed to improve productivity, optimize
utilization & efficiency, and simplify administration for
HPC clusters, clouds and supercomputers.

%package %{pbs_server}
Summary: PBS Professional for a server host
Group: ohpc/rms
Conflicts: pbspro-client-ohpc
Conflicts: pbspro-execution-ohpc
Conflicts: pbspro-client
Conflicts: pbspro-execution
Conflicts: pbspro-server
Conflicts: pbs
Conflicts: pbs-mom
Conflicts: pbs-cmds
Requires: expat
Requires: libedit
Requires: postgresql-server
Requires: python >= 2.6
Requires: python < 3.0
Requires: sendmail
Requires: tcl
Requires: tk
%if %{defined suse_version}
Requires: libical1
%else
Requires: libical
%endif
Autoreq: 1

%description %{pbs_server}
PBS Professional® is a fast, powerful workload manager and
job scheduler designed to improve productivity, optimize
utilization & efficiency, and simplify administration for
HPC clusters, clouds and supercomputers.

This package is intended for a server host. It includes all
PBS Professional components.

%package %{pbs_execution}
Summary: PBS Professional for an execution host
Group: ohpc/rms
Conflicts: pbspro-client-ohpc
Conflicts: pbspro-server-ohpc
Conflicts: pbspro-client
Conflicts: pbspro-execution
Conflicts: pbspro-server
Conflicts: pbs
Conflicts: pbs-mom
Conflicts: pbs-cmds
Requires: expat
Requires: python >= 2.6
Requires: python < 3.0
Autoreq: 1

%description %{pbs_execution}
PBS Professional® is a fast, powerful workload manager and
job scheduler designed to improve productivity, optimize
utilization & efficiency, and simplify administration for
HPC clusters, clouds and supercomputers.

This package is intended for an execution host. It does not
include the scheduler, server, or communication agent. It
does include the PBS Professional user commands.

%package %{pbs_client}
Summary: PBS Professional for a client host
Group: ohpc/rms
Conflicts: pbspro-execution-ohpc
Conflicts: pbspro-server-ohpc
Conflicts: pbspro-client
Conflicts: pbspro-execution
Conflicts: pbspro-server
Conflicts: pbs
Conflicts: pbs-mom
Conflicts: pbs-cmds
Requires: python >= 2.6
Requires: python < 3.0
Autoreq: 1

%description %{pbs_client}
PBS Professional® is a fast, powerful workload manager and
job scheduler designed to improve productivity, optimize
utilization & efficiency, and simplify administration for
HPC clusters, clouds and supercomputers.

This package is intended for a client host and provides
the PBS Professional user commands.

%if %{defined suse_version}
%debug_package
%endif

%prep
%setup

%build
[ -d build ] && rm -rf build
mkdir build
cd build
../configure \
	PBS_VERSION=%{version} \
	--prefix=%{pbs_prefix} \
%if %{with alps}
	--enable-alps \
%endif
%if %{with cpuset}
	--enable-cpuset \
%endif
%if %{with ibm-hps}
	--enable-hps \
%endif
%if %{with ibm-ib}
	--enable-aixib \
%endif
	--with-pbs-server-home=%{pbs_home} \
	--with-database-user=%{pbs_dbuser}
%{__make} %{?_smp_mflags}

%install
cd build
%make_install

%post %{pbs_server}
${RPM_INSTALL_PREFIX:=%{pbs_prefix}}/libexec/pbs_postinstall server \
	%{version} ${RPM_INSTALL_PREFIX:=%{pbs_prefix}} %{pbs_home} %{pbs_dbuser}

%post %{pbs_execution}
${RPM_INSTALL_PREFIX:=%{pbs_prefix}}/libexec/pbs_postinstall execution \
	%{version} ${RPM_INSTALL_PREFIX:=%{pbs_prefix}} %{pbs_home}

%post %{pbs_client}
${RPM_INSTALL_PREFIX:=%{pbs_prefix}}/libexec/pbs_postinstall client \
	%{version} ${RPM_INSTALL_PREFIX:=%{pbs_prefix}}

%preun %{pbs_server}
if [ -x /sbin/chkconfig -a -x /sbin/service ]; then
	out=`/sbin/chkconfig --list pbs 2>/dev/null`
	if [ $? -eq 0 ]; then
		if [ -x /etc/init.d/pbs ]; then
			/etc/init.d/pbs stop
		else
			/sbin/service pbs stop
		fi
		/sbin/chkconfig --del pbs
	fi
else
	[ -x /etc/init.d/pbs ] && /etc/init.d/pbs stop
	rm -f /etc/rc.d/rc0.d/K10pbs
	rm -f /etc/rc.d/rc1.d/K10pbs
	rm -f /etc/rc.d/rc2.d/K10pbs
	rm -f /etc/rc.d/rc3.d/S90pbs
	rm -f /etc/rc.d/rc4.d/K10pbs
	rm -f /etc/rc.d/rc5.d/S90pbs
	rm -f /etc/rc.d/rc6.d/K10pbs
fi
rm -f ${RPM_INSTALL_PREFIX:=%{pbs_prefix}}/etc/db_user.new
if [ `basename ${RPM_INSTALL_PREFIX:=%{pbs_prefix}}` = %{version} ]; then
	top_level=`dirname ${RPM_INSTALL_PREFIX:=%{pbs_prefix}}`
	if [ -h $top_level/default ]; then
		link_target=`readlink $top_level/default`
		[ `basename "$link_target"` = %{version} ] && rm -f $top_level/default
	fi
fi
rm -f /etc/init.d/pbs

%preun %{pbs_execution}
if [ -x /sbin/chkconfig -a -x /sbin/service ]; then
	out=`/sbin/chkconfig --list pbs 2>/dev/null`
	if [ $? -eq 0 ]; then
		if [ -x /etc/init.d/pbs ]; then
			/etc/init.d/pbs stop
		else
			/sbin/service pbs stop
		fi
		/sbin/chkconfig --del pbs
	fi
else
	[ -x /etc/init.d/pbs ] && /etc/init.d/pbs stop
	rm -f /etc/rc.d/rc0.d/K10pbs
	rm -f /etc/rc.d/rc1.d/K10pbs
	rm -f /etc/rc.d/rc2.d/K10pbs
	rm -f /etc/rc.d/rc3.d/S90pbs
	rm -f /etc/rc.d/rc4.d/K10pbs
	rm -f /etc/rc.d/rc5.d/S90pbs
	rm -f /etc/rc.d/rc6.d/K10pbs
fi
if [ `basename ${RPM_INSTALL_PREFIX:=%{pbs_prefix}}` = %{version} ]; then
	top_level=`dirname ${RPM_INSTALL_PREFIX:=%{pbs_prefix}}`
	if [ -h $top_level/default ]; then
		link_target=`readlink $top_level/default`
		[ `basename "$link_target"` = %{version} ] && rm -f $top_level/default
	fi
fi
rm -f /etc/init.d/pbs

%preun %{pbs_client}
if [ `basename ${RPM_INSTALL_PREFIX:=%{pbs_prefix}}` = %{version} ]; then
	top_level=`dirname ${RPM_INSTALL_PREFIX:=%{pbs_prefix}}`
	if [ -h $top_level/default ]; then
		link_target=`readlink $top_level/default`
		[ `basename "$link_target"` = %{version} ] && rm -f $top_level/default
	fi
fi

%postun %{pbs_server}
echo
echo "NOTE: /etc/pbs.conf and the PBS_HOME directory must be deleted manually"
echo

%postun %{pbs_execution}
echo
echo "NOTE: /etc/pbs.conf and the PBS_HOME directory must be deleted manually"
echo

%postun %{pbs_client}
echo
echo "NOTE: /etc/pbs.conf must be deleted manually"
echo

%files %{pbs_server}
%defattr(-,root,root, -)
%dir %{OHPC_HOME}
%dir %{OHPC_PUB}
%dir %{pbs_prefix}
%{pbs_prefix}/*
%attr(4755, root, root) %{pbs_prefix}/sbin/pbs_rcp
%attr(4755, root, root) %{pbs_prefix}/sbin/pbs_iff
%{_sysconfdir}/profile.d/pbs.csh
%{_sysconfdir}/profile.d/pbs.sh
# %{_sysconfdir}/init.d/pbs

%files %{pbs_execution}
%defattr(-,root,root, -)
%dir %{OHPC_HOME}
%dir %{OHPC_PUB}
%dir %{pbs_prefix}
%{pbs_prefix}/*
%attr(4755, root, root) %{pbs_prefix}/sbin/pbs_rcp
%attr(4755, root, root) %{pbs_prefix}/sbin/pbs_iff
%{_sysconfdir}/profile.d/pbs.csh
%{_sysconfdir}/profile.d/pbs.sh
# %{_sysconfdir}/init.d/pbs
%exclude %{pbs_prefix}/bin/printjob_svr.bin
%exclude %{pbs_prefix}/etc/pbs_db_schema.sql
%exclude %{pbs_prefix}/etc/pbs_dedicated
%exclude %{pbs_prefix}/etc/pbs_holidays*
%exclude %{pbs_prefix}/etc/pbs_resource_group
%exclude %{pbs_prefix}/etc/pbs_sched_config
%exclude %{pbs_prefix}/lib*/init.d/sgiICEplacement.sh
%exclude %{pbs_prefix}/lib*/python/altair/pbs_hooks/*
%exclude %{pbs_prefix}/libexec/install_db
%exclude %{pbs_prefix}/sbin/pbs_comm
%exclude %{pbs_prefix}/sbin/pbs_dataservice
%exclude %{pbs_prefix}/sbin/pbs_ds_monitor
%exclude %{pbs_prefix}/sbin/pbs_ds_password
%exclude %{pbs_prefix}/sbin/pbs_ds_password.bin
%exclude %{pbs_prefix}/sbin/pbs_sched
%exclude %{pbs_prefix}/sbin/pbs_server
%exclude %{pbs_prefix}/sbin/pbs_server.bin
%exclude %{pbs_prefix}/sbin/pbsfs

%files %{pbs_client}
%defattr(-,root,root, -)
%dir %{OHPC_HOME}
%dir %{OHPC_PUB}
%dir %{pbs_prefix}
%{pbs_prefix}/*
%attr(4755, root, root) %{pbs_prefix}/sbin/pbs_iff
%{_sysconfdir}/profile.d/pbs.csh
%{_sysconfdir}/profile.d/pbs.sh
%exclude %{pbs_prefix}/bin/mpiexec
%exclude %{pbs_prefix}/bin/pbs_attach
%exclude %{pbs_prefix}/bin/pbs_tmrsh
%exclude %{pbs_prefix}/bin/printjob_svr.bin
%exclude %{pbs_prefix}/etc/pbs_db_schema.sql
%exclude %{pbs_prefix}/etc/pbs_dedicated
%exclude %{pbs_prefix}/etc/pbs_holidays*
%exclude %{pbs_prefix}/etc/pbs_resource_group
%exclude %{pbs_prefix}/etc/pbs_sched_config
%exclude %{pbs_prefix}/include
%exclude %{pbs_prefix}/lib*/MPI
%exclude %{pbs_prefix}/lib*/init.d
%exclude %{pbs_prefix}/lib*/python/altair/pbs_hooks
%exclude %{pbs_prefix}/lib*/python/pbs_bootcheck*
%exclude %{pbs_prefix}/libexec/install_db
%exclude %{pbs_prefix}/libexec/pbs_habitat
%exclude %{pbs_prefix}/libexec/pbs_init.d
%exclude %{pbs_prefix}/sbin/pbs_comm
%exclude %{pbs_prefix}/sbin/pbs_demux
%exclude %{pbs_prefix}/sbin/pbs_dataservice
%exclude %{pbs_prefix}/sbin/pbs_ds_monitor
%exclude %{pbs_prefix}/sbin/pbs_ds_password
%exclude %{pbs_prefix}/sbin/pbs_ds_password.bin
%exclude %{pbs_prefix}/sbin/pbs_idled
%exclude %{pbs_prefix}/sbin/pbs_mom
%exclude %{pbs_prefix}/sbin/pbs_rcp
%exclude %{pbs_prefix}/sbin/pbs_sched
%exclude %{pbs_prefix}/sbin/pbs_server
%exclude %{pbs_prefix}/sbin/pbs_server.bin
%exclude %{pbs_prefix}/sbin/pbs_upgrade_job
%exclude %{pbs_prefix}/sbin/pbsfs

