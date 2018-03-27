import pandas as pd

if __name__ == "__main__":
    data = pd.read_csv("data/CRDC2013_14.csv", encoding ="Latin-1")
    
    data["total_enrollment"] = data["TOT_ENR_M"] + data["TOT_ENR_F"]
    all_enrollment = data["total_enrollment"].sum()
    
    total_m = data["TOT_ENR_M"].sum()
    total_f = data["TOT_ENR_F"].sum()
    
    m_percent = total_m / all_enrollment * 100
    f_percent = total_f / all_enrollment * 100
    
    total_hi = (data["SCH_ENR_HI_M"] + data["SCH_ENR_HI_F"]).sum()
    hi_percent = total_hi / all_enrollment * 100
    
    total_am = (data["SCH_ENR_AM_M"] + data["SCH_ENR_AM_F"]).sum()
    am_percent = total_am / all_enrollment * 100
    
    total_as = (data["SCH_ENR_AS_M"] + data["SCH_ENR_AS_F"]).sum()
    as_percent = total_as / all_enrollment * 100
    
    total_hp = (data["SCH_ENR_HP_M"] + data["SCH_ENR_HP_F"]).sum()
    hp_percent = total_hp / all_enrollment * 100
    
    total_bl = (data["SCH_ENR_BL_M"] + data["SCH_ENR_BL_F"]).sum()
    bl_percent = total_bl / all_enrollment * 100
    
    total_wh = (data["SCH_ENR_WH_M"] + data["SCH_ENR_WH_F"]).sum()
    wh_percent = total_wh / all_enrollment * 100
    
    total_tr = (data["SCH_ENR_TR_M"] + data["SCH_ENR_TR_F"]).sum()
    tr_percent = total_tr / all_enrollment * 100
    
    demo = {
        "Percent Male": m_percent,
        "Percent Female": f_percent,
        "Percent Hispanic": hi_percent,
        "Percent American Indian": am_percent,
        "Percent Asian": as_percent,
        "Percent Hawaiian/PIsland": hp_percent,
        "Percent Black": bl_percent,
        "Percent White": wh_percent,
        "Percent mixed": tr_percent}
    
    for k, v in demo.items():
        print(k, "is ", v)