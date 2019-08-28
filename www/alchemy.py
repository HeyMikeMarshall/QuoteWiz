def getEditions():
        import sqlalchemy
        from sqlalchemy.ext.automap import automap_base
        from sqlalchemy.orm import Session
        from sqlalchemy import create_engine, func, inspect, MetaData
        from config import local_db

        engine = create_engine(local_db)
        
        Base = automap_base(bind=engine)
        Base.prepare(engine, reflect=True)

        DPitems = Base.classes.dp_items
        session = Session(engine)
        
        query = session.query(DPitems.friendlyname).filter(DPitems.category == 'BASE').filter(DPitems.subcategory == 'CORE').all()
        print(query)
        results = []
        for item in query:
                results.append(item[0])
                
        session.commit()
        engine.dispose()
        
        return results

def getEditionDetails(edition):
        import sqlalchemy
        from sqlalchemy.ext.automap import automap_base
        from sqlalchemy.orm import Session
        from sqlalchemy import create_engine, func, inspect, MetaData
        from config import local_db
        engine = create_engine(local_db)
        
        Base = automap_base(bind=engine)
        Base.prepare(engine, reflect=True)

        DP_nodes = Base.classes.dp_nodes
        DPitems = Base.classes.dispatcher_phoenix
        DP_coreopts = Base.classes.dp_coreopts
        session = Session(engine)
        
        conf_query = session.query(DPitems.sap_num, DPitems.item_desc, DPitems.plist, DPitems.friendlyname)\
                .filter(DPitems.friendlyname == edition)\
                .all()
        
        pconf = {"item_num":conf_query[0][0],"desc":conf_query[0][1], "price":conf_query[0][2]}
    
        if edition == 'Foundations':
                node_query = session.query(DP_nodes.friendlyname, DP_nodes.node_type)\
                        .filter(DP_nodes.ed_foundations == True)\
                        .all()
                opt_query = session.query(DP_coreopts.friendlyname, DP_coreopts.shortid).filter(DP_coreopts.foundations == 'true').all()
    
        elif edition == 'Professional':
                node_query = session.query(DP_nodes.friendlyname, DP_nodes.node_type)\
                        .filter(DP_nodes.ed_professional == True)\
                        .all()
                opt_query = session.query(DP_coreopts.friendlyname, DP_coreopts.shortid)\
                        .filter(DP_coreopts.professional == 'true').all()
                
        elif edition == 'Office':
                node_query = session.query(DP_nodes.friendlyname, DP_nodes.node_type)\
                        .filter(DP_nodes.ed_office == True)\
                        .all()
                opt_query = session.query(DP_coreopts.friendlyname, DP_coreopts.shortid)\
                        .filter(DP_coreopts.office == 'true').all()

        elif edition == 'Legal':
                node_query = session.query(DP_nodes.friendlyname, DP_nodes.node_type)\
                        .filter(DP_nodes.ed_legal == True)\
                        .all()
                opt_query = session.query(DP_coreopts.friendlyname, DP_coreopts.shortid)\
                        .filter(DP_coreopts.legal == 'true').all()
        
        elif edition == 'Healthcare':
                node_query = session.query(DP_nodes.friendlyname, DP_nodes.node_type)\
                        .filter(DP_nodes.ed_healthcare == True)\
                        .all()
                opt_query = session.query(DP_coreopts.friendlyname, DP_coreopts.shortid)\
                        .filter(DP_coreopts.healthcare == 'true').all()
        
        elif edition == 'Government':
                node_query = session.query(DP_nodes.friendlyname, DP_nodes.node_type)\
                        .filter(DP_nodes.ed_government == True)\
                        .all()
                opt_query = session.query(DP_coreopts.friendlyname, DP_coreopts.shortid)\
                        .filter(DP_coreopts.government == 'true').all()
        
        elif edition == 'Finance':
                node_query = session.query(DP_nodes.friendlyname, DP_nodes.node_type)\
                        .filter(DP_nodes.ed_finance == True)\
                        .all()
                opt_query = session.query(DP_coreopts.friendlyname, DP_coreopts.shortid)\
                        .filter(DP_coreopts.finance == 'true').all()
        
        elif edition == 'Education':
                node_query = session.query(DP_nodes.friendlyname, DP_nodes.node_type)\
                        .filter(DP_nodes.ed_education == True)\
                        .all()
                opt_query = session.query(DP_coreopts.friendlyname, DP_coreopts.shortid)\
                        .filter(DP_coreopts.education == 'true').all()
                
        elif edition == 'ECM':
                node_query = session.query(DP_nodes.friendlyname, DP_nodes.node_type)\
                        .filter(DP_nodes.ed_ecm == True)\
                        .all()
                opt_query = session.query(DP_coreopts.friendlyname, DP_coreopts.shortid)\
                        .filter(DP_coreopts.ecma == 'true').all()

        elif edition == 'ECM Basic':
                node_query = session.query(DP_nodes.friendlyname, DP_nodes.node_type)\
                        .filter(DP_nodes.ed_ecm_basic == True)\
                        .all()
                opt_query = session.query(DP_coreopts.friendlyname, DP_coreopts.shortid)\
                        .filter(DP_coreopts.ecmb == 'true').all()
                
        elif edition == 'AccurioPro Connect':
                node_query = session.query(DP_nodes.friendlyname, DP_nodes.node_type)\
                        .filter(DP_nodes.ed_ecm_basic == True)\
                        .all()
                opt_query = session.query(DP_coreopts.friendlyname, DP_coreopts.shortid)\
                        .filter(DP_coreopts.acpconn == 'true').all()
                
        input_nodes = []
        process_nodes = []
        distribute_nodes = []
    
        for item in node_query:
                if item[1] == 'input':
                        input_nodes.append(item[0])
                if item[1] == 'process':
                        process_nodes.append(item[0])
                if item[1] == 'distribute':
                        distribute_nodes.append(item[0])
                
        result = {'pconf':pconf,
                'inc_opts':opt_query,
                        'inc_nodes':{'input':input_nodes,
                'process':process_nodes,
                'distribute':distribute_nodes}}
    
        session.commit()
        engine.dispose()
        
        return result

def insertQuote(data):
        import sqlalchemy
        from sqlalchemy.ext.automap import automap_base
        from sqlalchemy.orm import Session
        from sqlalchemy import create_engine, insert
        from datetime import datetime
        from config import local_db

        engine = create_engine(local_db)

        Base = automap_base(bind=engine)
        Base.prepare(engine, reflect=True)

        DPquotes = Base.classes.dp_quotes
        session = Session(engine)
        sys_timestamp=str(datetime.now())
        bsc_name=data.get('bsc-name', None)
        newQuote = DPquotes(bsc_name=bsc_name,
                        rep_name=data.get('rep-name', None),
                        cx_name=data.get('client-name', None),
                        cx_sapid=data.get('sap-id', None),
                        sys_timestamp=sys_timestamp,
                        quote_date=data.get("quote-date", None),
                        batch_users=data.get("batch-users",None),
                        dp_edition=data.get('edition', None),
                        ent_failover=data.get('ent-failover', None),
                        ent_failover_count=data.get('ent-failover-count', None),
                        ent_multi=data.get('ent-multi',None),
                        ent_multi_count=data.get('ent-multi-count',None),
                        ent_offloadmfp_count=data.get('ent-offloadmfp-count',None),
                        ent_offloadmobile_count=data.get('ent-offloadmobile-count',None),
                        ent_offloadweb_count=data.get('ent-offloadweb-count',None),
                        ent_workflowa_count=data.get('ent-workflowa-count',None),
                        ent_workflowb_count=data.get('ent-workflowb-count',None),
                        input_count=data.get('input-count',None),
                        maint_years=data.get('maint-years',None),
                        mobile_users=data.get('mobile-users',None),
                        offloadmfp=data.get('offloadmfp',None),
                        offloadmobile=data.get('offloadmobile',None),
                        offloadweb=data.get('offloadweb',None),
                        option_barcode1d=data.get('option-barcode1d',None),
                        option_barcode2d=data.get('option-barcode2d',None),
                        option_acpupgrade=data.get('option-acpupgrade',None),
                        option_advbates=data.get('option-advbates',None),
                        option_advocr=data.get('option-advocr',None),
                        batchindex=data.get('batchindex',None),
                        option_bookbildbndl=data.get('option-bookbildbndl',None),
                        option_bubgrader=data.get('option-bubgrader',None),
                        option_connconn=data.get('option-connconn',None),
                        option_convoffice=data.get('option-convoffice',None),
                        option_convpdf=data.get('option-convpdf',None),
                        option_copydef=data.get('option-copydef',None),
                        option_distrobndl=data.get('option-distrobndl',None),
                        option_dropboxin=data.get('option-dropboxin',None),
                        option_emailbndl=data.get('option-emailbndl',None),
                        option_fileparse=data.get('option-fileparse',None),
                        option_fluxconn=data.get('option-fluxconn',None),
                        option_formsproc=data.get('option-formsproc',None),
                        option_hl7=data.get('option-hl7',None),
                        option_hsredact=data.get('option-hsredact',None),
                        option_kdkgencon=data.get('option-kdkgencon',None),
                        option_laserfiche=data.get('option-laserfiche',None),
                        option_lprinput=data.get('option-lprinput',None),
                        option_metabndl=data.get('option-metabndl',None),
                        mobile=data.get('mobile',None),
                        option_ocrasiafont=data.get('option-ocrasiafont',None),
                        option_odbc=data.get('option-odbc',None),
                        option_onbase=data.get('option-onbase',None),
                        option_pdfproc=data.get('option-pdfproc',None),
                        option_pgcolroute=data.get('option-pgcolroute',None),
                        option_powertools=data.get('option-powertools',None),
                        option_printfile=data.get('option-printfile',None),
                        release2me=data.get('release2me',None),
                        option_rxshield=data.get('option-rxshield',None),
                        option_sharepoint=data.get('option-sharepoint',None),
                        option_winfax=data.get('option-winfax',None),
                        option_workshare=data.get('option-workshare',None),
                        workstation=data.get('workstation',None),
                        option_worldox=data.get('option-worldox',None),
                        price_level=data.get('price-level',None),
                        release2me_devices=data.get('release2me-devices',None),
                        workflowa=data.get('workflowa',None),
                        workflowb=data.get('workflowb',None),
                        workstation_users=data.get('workstation-users',None),
                        sec_consult=data.get('sec-consult-hours',None),
                        sec_develop=data.get('sec-develop-hours',None),
                        kmbs_install=data.get('kmbs-install-hours',None),
                        sec_remote=data.get('sec-remote',None)
                        )
        session.add(newQuote)
        session.commit()

        session = Session(engine)
        query = session.query(DPquotes.quote_id).filter(DPquotes.sys_timestamp == sys_timestamp).filter(DPquotes.bsc_name == bsc_name).one()
        session.commit()
        engine.dispose()

        return query[0]

def getMSQuote(quote_id):
        import sqlalchemy
        from sqlalchemy.ext.automap import automap_base
        from sqlalchemy.orm import Session
        from sqlalchemy import create_engine, func, inspect, MetaData
        from splinter import Browser
        import pandas as pd
        import time
        import re
        from config import local_db

        engine = create_engine(local_db)

        Base = automap_base(bind=engine)
        Base.prepare(engine, reflect=True)

        DPitems = Base.classes.dp_items
        MSquotes = Base.classes.ms_quotes
        session = Session(engine)

        query = session.query(MSquotes).filter(MSquotes.quote_id == quote_id).one()

        data = query.__dict__

        

        executable_path = {'executable_path': '/usr/local/bin/chromedriver'}

        browser = Browser('chrome', **executable_path, headless=True)

        browser.visit(data['maint_url'])
        time.sleep(1)

        scope = browser.find_by_tag("table").find_by_css(".ng-scope")
        edition = browser.find_by_css(".label")[0].text

        scopelist = []
        for item in scope:
                itemid = re.match(r"(^\d+)\s*\:\s*(.+)\s\(\s*(\d)", item.text)
                
                if itemid != None:
                        scopelist.append([itemid[1], itemid[3]])
                else:
                        continue
                
        browser.quit()
        scope_df = pd.DataFrame(scopelist, columns=['itemno', 'ms'])
        vcounts_df = pd.DataFrame(scope_df['itemno'].value_counts()).rename(columns={"itemno":"qty"}).reset_index(drop=False)
        scope_df = scope_df.drop_duplicates().sort_values('itemno').reset_index(drop=True)
        scope_df['qty']=vcounts_df['qty']
        scope_df['ms'] = scope_df['ms'].astype('int32')
        res_df = scope_df.loc[scope_df['ms']==data['maint_years']].reset_index(drop=True)


        df=pd.DataFrame()


        for item in res_df['itemno']:
                qty = int(res_df.loc[res_df['itemno'] == item]['qty'])
                sap_num = int(res_df.loc[res_df['itemno'] == item]['itemno'])
        
                query = session.query(DPitems.sap_num, DPitems.item_desc, DPitems.plist, DPitems.friendlyname, DPitems.shortid)\
                                                .filter(DPitems.sap_num == sap_num)\
                                                .all()
                core_dict = {'sap_num':str(query[0][0]),
                                                'item_desc':query[0][1],
                                                'price':query[0][2],
                                                'fname':query[0][3],
                                                'shortid':query[0][4],
                                                'qty':qty}

                df = df.append(core_dict, ignore_index=True)
        
        df['ext_price'] = df['price'] * df['qty']
        config = df.to_dict(orient='records')
        total_price = df['ext_price'].sum()
        result = {"total_price":total_price,
                        "quote_id":data['quote_id'],
                        "bsc_name":data['bsc_name'],
                        "rep_name":data['rep_name'],
                        "cx_name":data['cx_name'],
                        "cx_sapid":data['cx_sapid'],
                        "quote_date":data['quote_date'],
                        "maint_url":data['maint_url'],
                        "maint_years":data['maint_years'],
                        "unlock":data['unlock'],
                        "rid":data['rid'],
                        "mrid":data['mrid'],
                        "pcode":data['pcode'],
                        "edition":edition,
                        "config":config
                        }

        session.commit()
        engine.dispose()

        return result

def insertMSQuote(data):
        import sqlalchemy
        from sqlalchemy.ext.automap import automap_base
        from sqlalchemy.orm import Session
        from sqlalchemy import create_engine, insert
        from datetime import datetime
        import time
        import re


        engine = create_engine(local_db)

        Base = automap_base(bind=engine)
        Base.prepare(engine, reflect=True)

        MSquotes = Base.classes.ms_quotes
        session = Session(engine)
        sys_timestamp=str(datetime.now())
        bsc_name=data.get('bsc-name', None)

        maint_url = data.get('maint-url',None)

        def parseUrl(url):
                iparams = ["unlock","rid","mrid","pcode"]
                oparams = {}
                for param in iparams:
                        x = re.search(rf"{param}=([\w\-]*)", url).group(1)
                        oparams.update({param:x})
                return oparams
        uparams = parseUrl(maint_url)
        


        newQuote = MSquotes(bsc_name=bsc_name,
                        rep_name=data.get('rep-name', None),
                        cx_name=data.get('client-name', None),
                        cx_sapid=data.get('sap-id', None),
                        sys_timestamp=sys_timestamp,
                        quote_date=data.get("quote-date", None),
                        maint_years=data.get('maint-years',None),
                        maint_url=data.get('maint-url',None),
                        rid = uparams['rid'],
                        mrid = uparams['mrid'],
                        unlock = uparams['unlock'],
                        pcode = uparams['pcode']
                        )

        session.add(newQuote)
        query = session.query(MSquotes.quote_id).filter(MSquotes.sys_timestamp == sys_timestamp).filter(MSquotes.bsc_name == bsc_name).one()
        session.commit()
        engine.dispose()
        return query[0]

def getQuote(quote_id):  
        import sqlalchemy
        from sqlalchemy.ext.automap import automap_base
        from sqlalchemy.orm import Session
        from sqlalchemy import create_engine, func, inspect, MetaData
        import pandas as pd


        engine = create_engine(local_db)

        Base = automap_base(bind=engine)
        Base.prepare(engine, reflect=True)

        DPquotes = Base.classes.dp_quotes
        session = Session(engine)

        query = session.query(DPquotes).filter(DPquotes.quote_id == quote_id).one()

        data = query.__dict__

        options = []
        for item, state in data.items():
                if state == 'on':
                        spl_option = item.split('_')
                        if spl_option[0] == 'option':
                                options.append(spl_option[1].upper()) 

       

        msufx= "-M" + str(data['maint_years'])

        countGrps = {"input_count":int(data['input_count']),
                        "mobile_users":int(data['mobile_users']),
                        "release2me_devices":int(data['release2me_devices']),
                        "batch_users":int(data['batch_users']),
                        "workstation_users":int(data['workstation_users'])}

        failoverCount = int(data["ent_failover_count"])

        serviceGrps = {"SEC-CONSULT":data['sec_consult'],
                        "SEC-DEVELOP":data['sec_develop'],
                        "KMBS-INSTALL":data['kmbs_install'],
                        "SEC-REMOTE":data['sec_remote']}
        # svcs = ['sec_consult','sec_develop','kmbs_install','sec_remote']
        # serviceGrps = {}
        # for svc in svcs:
        #         if data[svc] != None:
        #                 serviceGrps.update()
        

        multi_count = int(data["ent_multi_count"])

        offloadGrps = {
                "OFFLOADMFP":int(data["ent_offloadmfp_count"]),
                "OFFLOADMOBILE":int(data["ent_offloadmobile_count"]),
                "OFFLOADWEB":int(data["ent_offloadweb_count"]),
                "OFFLOADWORKFLOWA":int(data["ent_workflowa_count"]),
                "OFFLOADWORKFLOWB":int(data["ent_workflowb_count"])
                }
        def countBreaker(countGrps):
                counts = {}
                for grp in countGrps:
                        if countGrps[grp] > 0:
                                if grp == 'input_count':
                                        input_count= countGrps[grp]
                                        i_count = 0
                                        x_count = 0
                                        xxv_count = 0
                                        l_count = 0
                                        c_count = 0
                                        d_count = 0

                                        while input_count >= 500:
                                                d_count += 1
                                                input_count -= 500
                                        while input_count >= 100:
                                                c_count += 1
                                                input_count -= 100
                                        while input_count >= 50:
                                                l_count += 1
                                                input_count -= 50
                                        while input_count >= 25:
                                                xxv_count += 1
                                                input_count -= 25
                                        while input_count >= 10:
                                                x_count += 1
                                                input_count -= 10
                                        while input_count >= 1:
                                                i_count += 1
                                                input_count -= 1

                                        counts["ADDINPUT-1"] = i_count
                                        counts["ADDINPUT-10"] = x_count
                                        counts["ADDINPUT-25"] = xxv_count
                                        counts["ADDINPUT-50"]= l_count
                                        counts["ADDINPUT-100"] = c_count
                                        counts["ADDINPUT-500"] = d_count

                                if grp == 'mobile_users':
                                        mobile_count= countGrps[grp]
                                        x_count = 0
                                        xxv_count = 0
                                        l_count = 0
                                        c_count = 0
                                        ccl_count = 0
                                        d_count = 0
                                        m_count = 0

                                        while mobile_count >= 1000:
                                                m_count += 1
                                                mobile_count -= 1000
                                        while mobile_count >= 500:
                                                d_count += 1
                                                mobile_count -= 500
                                        while mobile_count >= 100:
                                                c_count += 1
                                                mobile_count -= 100
                                        while mobile_count >= 250:
                                                ccl_count += 1
                                                mobile_count -= 250
                                        while mobile_count >= 50:
                                                l_count += 1
                                                mobile_count -= 50
                                        while mobile_count >= 25:
                                                xxv_count += 1
                                                mobile_count -= 25
                                        while mobile_count >= 10:
                                                x_count += 1
                                                mobile_count -= 10
                                        if mobile_count < 10 and mobile_count > 0:
                                                x_count += 1
                                        counts["MOBILE-10"]  = x_count
                                        counts["MOBILE-25"]  = xxv_count
                                        counts["MOBILE-50"]  = l_count
                                        counts["MOBILE-100"] = c_count
                                        counts["MOBILE-250"] = ccl_count
                                        counts["MOBILE-500"] = d_count
                                        counts["MOBILE-1000"] = m_count

                                if grp == "release2me_devices":
                                        input_count= countGrps[grp]
                                        i_count = 0
                                        iii_count = 0
                                        v_count = 0
                                        x_count = 0
                                        xxv_count = 0
                                        l_count = 0
                                        c_count = 0
                                        d_count = 0

                                        while input_count >= 500:
                                                d_count += 1
                                                input_count -= 500
                                        while input_count >= 100:
                                                c_count += 1
                                                input_count -= 100
                                        while input_count >= 50:
                                                l_count += 1
                                                input_count -= 50
                                        while input_count >= 25:
                                                xxv_count += 1
                                                input_count -= 25
                                        while input_count >= 10:
                                                x_count += 1
                                                input_count -= 10
                                        while input_count >= 5:
                                                v_count += 1
                                                input_count -= 5
                                        while input_count >= 3:
                                                iii_count += 1
                                                input_count -= 3
                                        while input_count >= 1:
                                                i_count += 1
                                                input_count -= 1

                                        counts["RELEASE2ME-1"] = i_count
                                        counts["RELEASE2ME-3"] = iii_count
                                        counts["RELEASE2ME-5"] = v_count
                                        counts["RELEASE2ME-10"] = x_count
                                        counts["RELEASE2ME-25"] = xxv_count
                                        counts["RELEASE2ME-50"] = l_count
                                        counts["RELEASE2ME-100"] = c_count
                                        counts["RELEASE2ME-500"] = d_count

                                if grp == "batch_users":
                                        input_count=countGrps[grp]
                                        i_count = 0
                                        i_count_a = 0
                                        x_count = 0

                                        while input_count > 10:
                                                x_count += 1
                                                input_count -= 1
                                        while input_count > 1:
                                                i_count_a += 1
                                                input_count -= 1
                                        while input_count == 1:
                                                i_count += 1
                                                input_count -= 1

                                        counts["BATCHIND-1"] = i_count
                                        counts["BATCHIND-1-ADD"] = i_count_a
                                        counts["BATCHIND-10"] = x_count

                                if grp == "workstation_users":
                                        input_count=countGrps[grp]
                                        i_count = 0
                                        i_count_a = 0
                                        x_count = 0

                                        while input_count > 10:
                                                x_count += 1
                                                input_count -= 1
                                        while input_count > 1:
                                                i_count_a += 1
                                                input_count -= 1
                                        while input_count == 1:
                                                i_count += 1
                                                input_count -= 1

                                        counts["WORKSTN-1"] = i_count
                                        counts["WORKSTN-1-ADD"] = i_count_a
                                        counts["WORKSTN-10"] = x_count

                return counts

        def basicQuery(counts, df):
                for grp in counts:
                        if counts[grp] > 0:
                                query = session.query(DPitems.sap_num, DPitems.item_desc, DPitems.plist, DPitems.friendlyname, DPitems.shortid)\
                                                .filter(DPitems.shortid == grp)\
                                                .all()
                                core_dict = {'sap_num':query[0][0],
                                                'item_desc':query[0][1],
                                                'price':query[0][2],
                                                'fname':query[0][3],
                                                'shortid':query[0][4],
                                                'qty':(counts[grp])}
                                df = df.append(core_dict, ignore_index=True)

                return df

        def optionQuery(options, df):
                for option in options:
                        query = session.query(DPitems.sap_num, DPitems.item_desc, DPitems.plist, DPitems.friendlyname, DPitems.shortid)\
                                        .filter(DPitems.shortid == option)\
                                        .all()

                        core_dict = {'sap_num':query[0][0],
                                                'item_desc':query[0][1],
                                                'price':query[0][2],
                                                'fname':query[0][3],
                                                'shortid':query[0][4],
                                                'qty':1}
                        df = df.append(core_dict, ignore_index=True)

                return df
        
        def failoverQuery(failovercount, df):
                if failovercount > 0:
                        R2MFOdone=False

                        for shortid in df['shortid']:
                                if 'WINFAX' in shortid:
                                        continue
                                if 'PDFPROC' in shortid:
                                        continue
                                if 'LASERFICHE' in shortid:
                                        continue
                                if 'HL7' in shortid:
                                        continue
                                if 'DROPBOXIN' in shortid:
                                        continue
                                if 'ACPUPGRADE' in shortid:
                                        continue
                                if 'OFFLOAD' in shortid:
                                        continue
                                if 'RELEASE2ME' in shortid and R2MFOdone == True:
                                        continue
                                elif 'RELEASE2ME' in shortid and R2MFOdone == False:
                                        query = session.query(DPitems.sap_num, DPitems.item_desc, DPitems.plist, DPitems.friendlyname, DPitems.shortid)\
                                                .filter(DPitems.shortid == "RELEASE2ME-FAILOVER")\
                                                .all()
                                        R2MFOdone = True

                                else:
                                        query = session.query(DPitems.sap_num, DPitems.item_desc, DPitems.plist, DPitems.friendlyname, DPitems.shortid)\
                                                .filter(DPitems.shortid == shortid+"-FAILOVER")\
                                                .all()            
                        
                        core_dict = {'sap_num':query[0][0],
                                                'item_desc':query[0][1],
                                                'price':query[0][2],
                                                'fname':query[0][3],
                                                'shortid':query[0][4],
                                                'qty':failovercount}
                        df = df.append(core_dict, ignore_index=True)
                
                return df

        def maintenanceQuery(df):
                for shortid in df['shortid']:
                        mqty = int(df.loc[df['shortid']== shortid]['qty'])
                        query = session.query(DPitems.sap_num, DPitems.item_desc, DPitems.plist, DPitems.friendlyname, DPitems.shortid)\
                                        .filter(DPitems.shortid == shortid+msufx)\
                                        .all()
                        core_dict = {'sap_num':query[0][0],
                                                'item_desc':query[0][1],
                                                'price':query[0][2],
                                                'fname':query[0][3],
                                                'shortid':query[0][4],
                                                'qty':mqty}
                        df = df.append(core_dict, ignore_index=True)
                return df       


        def prosvcsQuery(serviceGrps, df):
                for service in serviceGrps:
                        print(service)
                        if serviceGrps[service] != 0:
                                print(serviceGrps[service])
                                if serviceGrps[service] == 0 or serviceGrps[service] == None:
                                        continue
                                elif serviceGrps[service] == "on":
                                        qty = 1
                                else:                                   
                                        qty = serviceGrps[service]
                                        

                                query = session.query(DPitems.sap_num, DPitems.item_desc, DPitems.plist, DPitems.friendlyname, DPitems.shortid)\
                                                        .filter(DPitems.shortid == service)\
                                                        .all()
                                core_dict = {'sap_num':query[0][0],
                                                        'item_desc':query[0][1],
                                                        'price':query[0][2],
                                                        'fname':query[0][3],
                                                        'shortid':query[0][4],
                                                        'qty':qty}
                                df = df.append(core_dict, ignore_index=True)
                return df       



        engine = create_engine(local_db)

        Base = automap_base(bind=engine)
        Base.prepare(engine, reflect=True)
        DP_nodes = Base.classes.dp_nodes
        DPitems = Base.classes.dp_items
        session = Session(engine)

        core_query = session.query(DPitems.sap_num, DPitems.item_desc, DPitems.plist, DPitems.friendlyname, DPitems.shortid)\
                .filter(DPitems.friendlyname == data["dp_edition"])\
                .all()
        core_dict = {'sap_num':core_query[0][0],
                'item_desc':core_query[0][1],
                'price':core_query[0][2],
                'fname':core_query[0][3],
                'shortid':core_query[0][4],
                'qty':1}


        df = pd.DataFrame(data=core_dict, index=[0])
        df = basicQuery(countBreaker(countGrps), df)
        df = basicQuery(offloadGrps, df)
        df = optionQuery(options, df)
        df = failoverQuery(failoverCount, df)
        df = maintenanceQuery(df)
        df = prosvcsQuery(serviceGrps, df)


        quote_id = data['quote_id']
        cx_name = data['cx_name']
        cx_sapid = data['cx_sapid']
        bsc_name = data['bsc_name']
        rep_name = data['rep_name']
        quote_date = data['quote_date']
        edition = data.get('dp_edition')


        if edition == 'Foundations':
                node_query = session.query(DP_nodes.friendlyname, DP_nodes.node_type)\
                        .filter(DP_nodes.ed_foundations == True)\
                        .all()
        
        elif edition == 'Professional':
                node_query = session.query(DP_nodes.friendlyname, DP_nodes.node_type)\
                        .filter(DP_nodes.ed_professional == True)\
                        .all()
                
        elif edition == 'Office':
                node_query = session.query(DP_nodes.friendlyname, DP_nodes.node_type)\
                        .filter(DP_nodes.ed_office == True)\
                        .all()

        elif edition == 'Legal':
                node_query = session.query(DP_nodes.friendlyname, DP_nodes.node_type)\
                        .filter(DP_nodes.ed_legal == True)\
                        .all()
        
        elif edition == 'Healthcare':
                node_query = session.query(DP_nodes.friendlyname, DP_nodes.node_type)\
                        .filter(DP_nodes.ed_healthcare == True)\
                        .all()
        
        elif edition == 'Government':
                node_query = session.query(DP_nodes.friendlyname, DP_nodes.node_type)\
                        .filter(DP_nodes.ed_government == True)\
                        .all()
        
        elif edition == 'Finance':
                node_query = session.query(DP_nodes.friendlyname, DP_nodes.node_type)\
                        .filter(DP_nodes.ed_finance == True)\
                        .all()
        
        elif edition == 'Education':
                node_query = session.query(DP_nodes.friendlyname, DP_nodes.node_type)\
                        .filter(DP_nodes.ed_education == True)\
                        .all()
                
        elif edition == 'ECM':
                node_query = session.query(DP_nodes.friendlyname, DP_nodes.node_type)\
                        .filter(DP_nodes.ed_ecm == True)\
                        .all()

        elif edition == 'ECM Basic':
                node_query = session.query(DP_nodes.friendlyname, DP_nodes.node_type)\
                        .filter(DP_nodes.ed_ecm_basic == True)\
                        .all()
                
        elif edition == 'AccurioPro Connect':
                node_query = session.query(DP_nodes.friendlyname, DP_nodes.node_type)\
                        .filter(DP_nodes.ed_ecm_basic == True)\
                        .all()
                
        input_nodes = []
        process_nodes = []
        distribute_nodes = []
        
        for item in node_query:
                if item[1] == 'input':
                        input_nodes.append(item[0])
                if item[1] == 'process':
                        process_nodes.append(item[0])
                if item[1] == 'distribute':
                        distribute_nodes.append(item[0])

        session.commit()
        engine.dispose()

        df['ext_price'] = df['price'] * df['qty']
        config = df.to_dict(orient='records')
        total_price = df['ext_price'].sum()
        result = {"quote_id":quote_id,
                "total_price":total_price,
                "edition":edition,
                "cx_name":cx_name,
                "cx_sapid":cx_sapid,
                "bsc_name":bsc_name,
                "rep_name":rep_name,
                "quote_date":quote_date,
                "nodes":{"input_nodes":input_nodes, "process_nodes":process_nodes, "distribute_nodes":distribute_nodes},
                "config":config}
        return result