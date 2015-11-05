import glob
import os
import logging
import sys

log = logging.getLogger(__name__)


def delete_logs():
    ret = {'deleted_logs' : []}
    try:
        tomcat_logs = glob.glob('/opt/*/tomcat/logs/*')
        for tomcat_log in tomcat_logs:
            log.info('deleting : ' + tomcat_log)
            os.remove(tomcat_log)
            ret['deleted_logs'].append(tomcat_log)
        ret['result'] = True
    except:
        log.error('Failed to delete tomcat logs : {}'.format(sys.exc_info()[0]))
        ret['comment'] = 'Failed to delete tomcat logs'
    return ret
