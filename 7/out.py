precalc = dict()
def bo_fn():
    result = precalc.get('bo_fn')
    if result is None:
        result = bn_fn() >> 2 
        precalc['bo_fn'] = result
    return result


def ly_fn():
    result = precalc.get('ly_fn')
    if result is None:
        result = lf_fn() >> 1 
        precalc['ly_fn'] = result
    return result


def fq_fn():
    result = precalc.get('fq_fn')
    if result is None:
        result = fo_fn() >> 3 
        precalc['fq_fn'] = result
    return result


def cq_fn():
    result = precalc.get('cq_fn')
    if result is None:
        result = cj_fn() | cp_fn() 
        precalc['cq_fn'] = result
    return result


def ga_fn():
    result = precalc.get('ga_fn')
    if result is None:
        result = fo_fn() | fz_fn() 
        precalc['ga_fn'] = result
    return result


def u_fn():
    result = precalc.get('u_fn')
    if result is None:
        result = t_fn() | s_fn() 
        precalc['u_fn'] = result
    return result


def a_fn():
    result = precalc.get('a_fn')
    if result is None:
        result = lx_fn() 
        precalc['a_fn'] = result
    return result


def ay_fn():
    result = precalc.get('ay_fn')
    if result is None:
        result = ~ ax_fn() 
        precalc['ay_fn'] = result
    return result


def hf_fn():
    result = precalc.get('hf_fn')
    if result is None:
        result = he_fn() >> 2 
        precalc['hf_fn'] = result
    return result


def lr_fn():
    result = precalc.get('lr_fn')
    if result is None:
        result = lf_fn() | lq_fn() 
        precalc['lr_fn'] = result
    return result


def lu_fn():
    result = precalc.get('lu_fn')
    if result is None:
        result = lr_fn() & lt_fn() 
        precalc['lu_fn'] = result
    return result


def ek_fn():
    result = precalc.get('ek_fn')
    if result is None:
        result = dy_fn() | ej_fn() 
        precalc['ek_fn'] = result
    return result


def cy_fn():
    result = precalc.get('cy_fn')
    if result is None:
        result = 1 & cx_fn() 
        precalc['cy_fn'] = result
    return result


def hv_fn():
    result = precalc.get('hv_fn')
    if result is None:
        result = hb_fn() << 1 
        precalc['hv_fn'] = result
    return result


def bi_fn():
    result = precalc.get('bi_fn')
    if result is None:
        result = 1 & bh_fn() 
        precalc['bi_fn'] = result
    return result


def ik_fn():
    result = precalc.get('ik_fn')
    if result is None:
        result = ih_fn() & ij_fn() 
        precalc['ik_fn'] = result
    return result


def t_fn():
    result = precalc.get('t_fn')
    if result is None:
        result = c_fn() << 1 
        precalc['t_fn'] = result
    return result


def ed_fn():
    result = precalc.get('ed_fn')
    if result is None:
        result = ea_fn() & eb_fn() 
        precalc['ed_fn'] = result
    return result


def ko_fn():
    result = precalc.get('ko_fn')
    if result is None:
        result = km_fn() | kn_fn() 
        precalc['ko_fn'] = result
    return result


def bx_fn():
    result = precalc.get('bx_fn')
    if result is None:
        result = ~ bw_fn() 
        precalc['bx_fn'] = result
    return result


def cu_fn():
    result = precalc.get('cu_fn')
    if result is None:
        result = ci_fn() | ct_fn() 
        precalc['cu_fn'] = result
    return result


def q_fn():
    result = precalc.get('q_fn')
    if result is None:
        result = ~ p_fn() 
        precalc['q_fn'] = result
    return result


def lx_fn():
    result = precalc.get('lx_fn')
    if result is None:
        result = lw_fn() | lv_fn() 
        precalc['lx_fn'] = result
    return result


def lp_fn():
    result = precalc.get('lp_fn')
    if result is None:
        result = ~ lo_fn() 
        precalc['lp_fn'] = result
    return result


def fw_fn():
    result = precalc.get('fw_fn')
    if result is None:
        result = fp_fn() | fv_fn() 
        precalc['fw_fn'] = result
    return result


def r_fn():
    result = precalc.get('r_fn')
    if result is None:
        result = o_fn() & q_fn() 
        precalc['r_fn'] = result
    return result


def dk_fn():
    result = precalc.get('dk_fn')
    if result is None:
        result = dh_fn() & dj_fn() 
        precalc['dk_fn'] = result
    return result


def bj_fn():
    result = precalc.get('bj_fn')
    if result is None:
        result = ap_fn() << 1 
        precalc['bj_fn'] = result
    return result


def ce_fn():
    result = precalc.get('ce_fn')
    if result is None:
        result = bk_fn() << 1 
        precalc['ce_fn'] = result
    return result


def ij_fn():
    result = precalc.get('ij_fn')
    if result is None:
        result = ~ ii_fn() 
        precalc['ij_fn'] = result
    return result


def gj_fn():
    result = precalc.get('gj_fn')
    if result is None:
        result = gh_fn() | gi_fn() 
        precalc['gj_fn'] = result
    return result


def ld_fn():
    result = precalc.get('ld_fn')
    if result is None:
        result = kk_fn() >> 1 
        precalc['ld_fn'] = result
    return result


def lw_fn():
    result = precalc.get('lw_fn')
    if result is None:
        result = lc_fn() << 1 
        precalc['lw_fn'] = result
    return result


def lc_fn():
    result = precalc.get('lc_fn')
    if result is None:
        result = lb_fn() | la_fn() 
        precalc['lc_fn'] = result
    return result


def an_fn():
    result = precalc.get('an_fn')
    if result is None:
        result = 1 & am_fn() 
        precalc['an_fn'] = result
    return result


def gq_fn():
    result = precalc.get('gq_fn')
    if result is None:
        result = gn_fn() & gp_fn() 
        precalc['gq_fn'] = result
    return result


def lh_fn():
    result = precalc.get('lh_fn')
    if result is None:
        result = lf_fn() >> 3 
        precalc['lh_fn'] = result
    return result


def g_fn():
    result = precalc.get('g_fn')
    if result is None:
        result = e_fn() | f_fn() 
        precalc['g_fn'] = result
    return result


def lo_fn():
    result = precalc.get('lo_fn')
    if result is None:
        result = lg_fn() & lm_fn() 
        precalc['lo_fn'] = result
    return result


def db_fn():
    result = precalc.get('db_fn')
    if result is None:
        result = ci_fn() >> 1 
        precalc['db_fn'] = result
    return result


def cz_fn():
    result = precalc.get('cz_fn')
    if result is None:
        result = cf_fn() << 1 
        precalc['cz_fn'] = result
    return result


def cg_fn():
    result = precalc.get('cg_fn')
    if result is None:
        result = bn_fn() >> 1 
        precalc['cg_fn'] = result
    return result


def fg_fn():
    result = precalc.get('fg_fn')
    if result is None:
        result = et_fn() & fe_fn() 
        precalc['fg_fn'] = result
    return result


def iu_fn():
    result = precalc.get('iu_fn')
    if result is None:
        result = is_fn() | it_fn() 
        precalc['iu_fn'] = result
    return result


def kz_fn():
    result = precalc.get('kz_fn')
    if result is None:
        result = kw_fn() & ky_fn() 
        precalc['kz_fn'] = result
    return result


def cn_fn():
    result = precalc.get('cn_fn')
    if result is None:
        result = ck_fn() & cl_fn() 
        precalc['cn_fn'] = result
    return result


def bk_fn():
    result = precalc.get('bk_fn')
    if result is None:
        result = bj_fn() | bi_fn() 
        precalc['bk_fn'] = result
    return result


def hc_fn():
    result = precalc.get('hc_fn')
    if result is None:
        result = gj_fn() >> 1 
        precalc['hc_fn'] = result
    return result


def jh_fn():
    result = precalc.get('jh_fn')
    if result is None:
        result = iu_fn() & jf_fn() 
        precalc['jh_fn'] = result
    return result


def bt_fn():
    result = precalc.get('bt_fn')
    if result is None:
        result = ~ bs_fn() 
        precalc['bt_fn'] = result
    return result


def kw_fn():
    result = precalc.get('kw_fn')
    if result is None:
        result = kk_fn() | kv_fn() 
        precalc['kw_fn'] = result
    return result


def kv_fn():
    result = precalc.get('kv_fn')
    if result is None:
        result = ks_fn() & ku_fn() 
        precalc['kv_fn'] = result
    return result


def il_fn():
    result = precalc.get('il_fn')
    if result is None:
        result = hz_fn() | ik_fn() 
        precalc['il_fn'] = result
    return result


def v_fn():
    result = precalc.get('v_fn')
    if result is None:
        result = b_fn() >> 1 
        precalc['v_fn'] = result
    return result


def jn_fn():
    result = precalc.get('jn_fn')
    if result is None:
        result = iu_fn() >> 1 
        precalc['jn_fn'] = result
    return result


def fr_fn():
    result = precalc.get('fr_fn')
    if result is None:
        result = fo_fn() >> 5 
        precalc['fr_fn'] = result
    return result


def bh_fn():
    result = precalc.get('bh_fn')
    if result is None:
        result = be_fn() & bg_fn() 
        precalc['bh_fn'] = result
    return result


def gd_fn():
    result = precalc.get('gd_fn')
    if result is None:
        result = ga_fn() & gc_fn() 
        precalc['gd_fn'] = result
    return result


def hm_fn():
    result = precalc.get('hm_fn')
    if result is None:
        result = hf_fn() | hl_fn() 
        precalc['hm_fn'] = result
    return result


def lf_fn():
    result = precalc.get('lf_fn')
    if result is None:
        result = ld_fn() | le_fn() 
        precalc['lf_fn'] = result
    return result


def av_fn():
    result = precalc.get('av_fn')
    if result is None:
        result = as_fn() >> 5 
        precalc['av_fn'] = result
    return result


def fo_fn():
    result = precalc.get('fo_fn')
    if result is None:
        result = fm_fn() | fn_fn() 
        precalc['fo_fn'] = result
    return result


def hp_fn():
    result = precalc.get('hp_fn')
    if result is None:
        result = hm_fn() & ho_fn() 
        precalc['hp_fn'] = result
    return result


def ln_fn():
    result = precalc.get('ln_fn')
    if result is None:
        result = lg_fn() | lm_fn() 
        precalc['ln_fn'] = result
    return result


def ky_fn():
    result = precalc.get('ky_fn')
    if result is None:
        result = ~ kx_fn() 
        precalc['ky_fn'] = result
    return result


def km_fn():
    result = precalc.get('km_fn')
    if result is None:
        result = kk_fn() >> 3 
        precalc['km_fn'] = result
    return result


def en_fn():
    result = precalc.get('en_fn')
    if result is None:
        result = ek_fn() & em_fn() 
        precalc['en_fn'] = result
    return result


def fu_fn():
    result = precalc.get('fu_fn')
    if result is None:
        result = ~ ft_fn() 
        precalc['fu_fn'] = result
    return result


def ji_fn():
    result = precalc.get('ji_fn')
    if result is None:
        result = ~ jh_fn() 
        precalc['ji_fn'] = result
    return result


def jp_fn():
    result = precalc.get('jp_fn')
    if result is None:
        result = jn_fn() | jo_fn() 
        precalc['jp_fn'] = result
    return result


def gw_fn():
    result = precalc.get('gw_fn')
    if result is None:
        result = gj_fn() & gu_fn() 
        precalc['gw_fn'] = result
    return result


def l_fn():
    result = precalc.get('l_fn')
    if result is None:
        result = d_fn() & j_fn() 
        precalc['l_fn'] = result
    return result


def fm_fn():
    result = precalc.get('fm_fn')
    if result is None:
        result = et_fn() >> 1 
        precalc['fm_fn'] = result
    return result


def jx_fn():
    result = precalc.get('jx_fn')
    if result is None:
        result = jq_fn() | jw_fn() 
        precalc['jx_fn'] = result
    return result


def eq_fn():
    result = precalc.get('eq_fn')
    if result is None:
        result = ep_fn() | eo_fn() 
        precalc['eq_fn'] = result
    return result


def lz_fn():
    result = precalc.get('lz_fn')
    if result is None:
        result = lv_fn() << 15 
        precalc['lz_fn'] = result
    return result


def ez_fn():
    result = precalc.get('ez_fn')
    if result is None:
        result = ~ ey_fn() 
        precalc['ez_fn'] = result
    return result


def jq_fn():
    result = precalc.get('jq_fn')
    if result is None:
        result = jp_fn() >> 2 
        precalc['jq_fn'] = result
    return result


def ej_fn():
    result = precalc.get('ej_fn')
    if result is None:
        result = eg_fn() & ei_fn() 
        precalc['ej_fn'] = result
    return result


def dn_fn():
    result = precalc.get('dn_fn')
    if result is None:
        result = ~ dm_fn() 
        precalc['dn_fn'] = result
    return result


def kc_fn():
    result = precalc.get('kc_fn')
    if result is None:
        result = jp_fn() & ka_fn() 
        precalc['kc_fn'] = result
    return result


def bf_fn():
    result = precalc.get('bf_fn')
    if result is None:
        result = as_fn() & bd_fn() 
        precalc['bf_fn'] = result
    return result


def fl_fn():
    result = precalc.get('fl_fn')
    if result is None:
        result = fk_fn() | fj_fn() 
        precalc['fl_fn'] = result
    return result


def dy_fn():
    result = precalc.get('dy_fn')
    if result is None:
        result = dw_fn() | dx_fn() 
        precalc['dy_fn'] = result
    return result


def lm_fn():
    result = precalc.get('lm_fn')
    if result is None:
        result = lj_fn() & ll_fn() 
        precalc['lm_fn'] = result
    return result


def ef_fn():
    result = precalc.get('ef_fn')
    if result is None:
        result = ec_fn() & ee_fn() 
        precalc['ef_fn'] = result
    return result


def ft_fn():
    result = precalc.get('ft_fn')
    if result is None:
        result = fq_fn() & fr_fn() 
        precalc['ft_fn'] = result
    return result


def kq_fn():
    result = precalc.get('kq_fn')
    if result is None:
        result = ~ kp_fn() 
        precalc['kq_fn'] = result
    return result


def kk_fn():
    result = precalc.get('kk_fn')
    if result is None:
        result = ki_fn() | kj_fn() 
        precalc['kk_fn'] = result
    return result


def da_fn():
    result = precalc.get('da_fn')
    if result is None:
        result = cz_fn() | cy_fn() 
        precalc['da_fn'] = result
    return result


def au_fn():
    result = precalc.get('au_fn')
    if result is None:
        result = as_fn() >> 3 
        precalc['au_fn'] = result
    return result


def ar_fn():
    result = precalc.get('ar_fn')
    if result is None:
        result = an_fn() << 15 
        precalc['ar_fn'] = result
    return result


def fn_fn():
    result = precalc.get('fn_fn')
    if result is None:
        result = fj_fn() << 15 
        precalc['fn_fn'] = result
    return result


def fj_fn():
    result = precalc.get('fj_fn')
    if result is None:
        result = 1 & fi_fn() 
        precalc['fj_fn'] = result
    return result


def hx_fn():
    result = precalc.get('hx_fn')
    if result is None:
        result = he_fn() >> 1 
        precalc['hx_fn'] = result
    return result


def lg_fn():
    result = precalc.get('lg_fn')
    if result is None:
        result = lf_fn() >> 2 
        precalc['lg_fn'] = result
    return result


def kj_fn():
    result = precalc.get('kj_fn')
    if result is None:
        result = kf_fn() << 15 
        precalc['kj_fn'] = result
    return result


def eh_fn():
    result = precalc.get('eh_fn')
    if result is None:
        result = dz_fn() & ef_fn() 
        precalc['eh_fn'] = result
    return result


def id_fn():
    result = precalc.get('id_fn')
    if result is None:
        result = ib_fn() | ic_fn() 
        precalc['id_fn'] = result
    return result


def li_fn():
    result = precalc.get('li_fn')
    if result is None:
        result = lf_fn() >> 5 
        precalc['li_fn'] = result
    return result


def br_fn():
    result = precalc.get('br_fn')
    if result is None:
        result = bp_fn() | bq_fn() 
        precalc['br_fn'] = result
    return result


def gt_fn():
    result = precalc.get('gt_fn')
    if result is None:
        result = ~ gs_fn() 
        precalc['gt_fn'] = result
    return result


def gh_fn():
    result = precalc.get('gh_fn')
    if result is None:
        result = fo_fn() >> 1 
        precalc['gh_fn'] = result
    return result


def cc_fn():
    result = precalc.get('cc_fn')
    if result is None:
        result = bz_fn() & cb_fn() 
        precalc['cc_fn'] = result
    return result


def ec_fn():
    result = precalc.get('ec_fn')
    if result is None:
        result = ea_fn() | eb_fn() 
        precalc['ec_fn'] = result
    return result


def ls_fn():
    result = precalc.get('ls_fn')
    if result is None:
        result = lf_fn() & lq_fn() 
        precalc['ls_fn'] = result
    return result


def m_fn():
    result = precalc.get('m_fn')
    if result is None:
        result = ~ l_fn() 
        precalc['m_fn'] = result
    return result


def ib_fn():
    result = precalc.get('ib_fn')
    if result is None:
        result = hz_fn() >> 3 
        precalc['ib_fn'] = result
    return result


def dj_fn():
    result = precalc.get('dj_fn')
    if result is None:
        result = ~ di_fn() 
        precalc['dj_fn'] = result
    return result


def ll_fn():
    result = precalc.get('ll_fn')
    if result is None:
        result = ~ lk_fn() 
        precalc['ll_fn'] = result
    return result


def jr_fn():
    result = precalc.get('jr_fn')
    if result is None:
        result = jp_fn() >> 3 
        precalc['jr_fn'] = result
    return result


def js_fn():
    result = precalc.get('js_fn')
    if result is None:
        result = jp_fn() >> 5 
        precalc['js_fn'] = result
    return result


def bg_fn():
    result = precalc.get('bg_fn')
    if result is None:
        result = ~ bf_fn() 
        precalc['bg_fn'] = result
    return result


def w_fn():
    result = precalc.get('w_fn')
    if result is None:
        result = s_fn() << 15 
        precalc['w_fn'] = result
    return result


def fk_fn():
    result = precalc.get('fk_fn')
    if result is None:
        result = eq_fn() << 1 
        precalc['fk_fn'] = result
    return result


def jm_fn():
    result = precalc.get('jm_fn')
    if result is None:
        result = jl_fn() | jk_fn() 
        precalc['jm_fn'] = result
    return result


def im_fn():
    result = precalc.get('im_fn')
    if result is None:
        result = hz_fn() & ik_fn() 
        precalc['im_fn'] = result
    return result


def eg_fn():
    result = precalc.get('eg_fn')
    if result is None:
        result = dz_fn() | ef_fn() 
        precalc['eg_fn'] = result
    return result


def gz_fn():
    result = precalc.get('gz_fn')
    if result is None:
        result = 1 & gy_fn() 
        precalc['gz_fn'] = result
    return result


def le_fn():
    result = precalc.get('le_fn')
    if result is None:
        result = la_fn() << 15 
        precalc['le_fn'] = result
    return result


def bu_fn():
    result = precalc.get('bu_fn')
    if result is None:
        result = br_fn() & bt_fn() 
        precalc['bu_fn'] = result
    return result


def co_fn():
    result = precalc.get('co_fn')
    if result is None:
        result = ~ cn_fn() 
        precalc['co_fn'] = result
    return result


def x_fn():
    result = precalc.get('x_fn')
    if result is None:
        result = v_fn() | w_fn() 
        precalc['x_fn'] = result
    return result


def k_fn():
    result = precalc.get('k_fn')
    if result is None:
        result = d_fn() | j_fn() 
        precalc['k_fn'] = result
    return result


def ge_fn():
    result = precalc.get('ge_fn')
    if result is None:
        result = 1 & gd_fn() 
        precalc['ge_fn'] = result
    return result


def ih_fn():
    result = precalc.get('ih_fn')
    if result is None:
        result = ia_fn() | ig_fn() 
        precalc['ih_fn'] = result
    return result


def gp_fn():
    result = precalc.get('gp_fn')
    if result is None:
        result = ~ go_fn() 
        precalc['gp_fn'] = result
    return result


def ee_fn():
    result = precalc.get('ee_fn')
    if result is None:
        result = ~ ed_fn() 
        precalc['ee_fn'] = result
    return result


def jy_fn():
    result = precalc.get('jy_fn')
    if result is None:
        result = jq_fn() & jw_fn() 
        precalc['jy_fn'] = result
    return result


def ff_fn():
    result = precalc.get('ff_fn')
    if result is None:
        result = et_fn() | fe_fn() 
        precalc['ff_fn'] = result
    return result


def az_fn():
    result = precalc.get('az_fn')
    if result is None:
        result = aw_fn() & ay_fn() 
        precalc['az_fn'] = result
    return result


def fi_fn():
    result = precalc.get('fi_fn')
    if result is None:
        result = ff_fn() & fh_fn() 
        precalc['fi_fn'] = result
    return result


def jl_fn():
    result = precalc.get('jl_fn')
    if result is None:
        result = ir_fn() << 1 
        precalc['jl_fn'] = result
    return result


def ha_fn():
    result = precalc.get('ha_fn')
    if result is None:
        result = gg_fn() << 1 
        precalc['ha_fn'] = result
    return result


def y_fn():
    result = precalc.get('y_fn')
    if result is None:
        result = x_fn() >> 2 
        precalc['y_fn'] = result
    return result


def dd_fn():
    result = precalc.get('dd_fn')
    if result is None:
        result = db_fn() | dc_fn() 
        precalc['dd_fn'] = result
    return result


def bn_fn():
    result = precalc.get('bn_fn')
    if result is None:
        result = bl_fn() | bm_fn() 
        precalc['bn_fn'] = result
    return result


def ie_fn():
    result = precalc.get('ie_fn')
    if result is None:
        result = ib_fn() & ic_fn() 
        precalc['ie_fn'] = result
    return result


def z_fn():
    result = precalc.get('z_fn')
    if result is None:
        result = x_fn() >> 3 
        precalc['z_fn'] = result
    return result


def lk_fn():
    result = precalc.get('lk_fn')
    if result is None:
        result = lh_fn() & li_fn() 
        precalc['lk_fn'] = result
    return result


def cf_fn():
    result = precalc.get('cf_fn')
    if result is None:
        result = ce_fn() | cd_fn() 
        precalc['cf_fn'] = result
    return result


def bc_fn():
    result = precalc.get('bc_fn')
    if result is None:
        result = ~ bb_fn() 
        precalc['bc_fn'] = result
    return result


def hl_fn():
    result = precalc.get('hl_fn')
    if result is None:
        result = hi_fn() & hk_fn() 
        precalc['hl_fn'] = result
    return result


def gc_fn():
    result = precalc.get('gc_fn')
    if result is None:
        result = ~ gb_fn() 
        precalc['gc_fn'] = result
    return result


def s_fn():
    result = precalc.get('s_fn')
    if result is None:
        result = 1 & r_fn() 
        precalc['s_fn'] = result
    return result


def fz_fn():
    result = precalc.get('fz_fn')
    if result is None:
        result = fw_fn() & fy_fn() 
        precalc['fz_fn'] = result
    return result


def fe_fn():
    result = precalc.get('fe_fn')
    if result is None:
        result = fb_fn() & fd_fn() 
        precalc['fe_fn'] = result
    return result


def eo_fn():
    result = precalc.get('eo_fn')
    if result is None:
        result = 1 & en_fn() 
        precalc['eo_fn'] = result
    return result


def ab_fn():
    result = precalc.get('ab_fn')
    if result is None:
        result = z_fn() | aa_fn() 
        precalc['ab_fn'] = result
    return result


def bm_fn():
    result = precalc.get('bm_fn')
    if result is None:
        result = bi_fn() << 15 
        precalc['bm_fn'] = result
    return result


def hi_fn():
    result = precalc.get('hi_fn')
    if result is None:
        result = hg_fn() | hh_fn() 
        precalc['hi_fn'] = result
    return result


def lb_fn():
    result = precalc.get('lb_fn')
    if result is None:
        result = kh_fn() << 1 
        precalc['lb_fn'] = result
    return result


def ci_fn():
    result = precalc.get('ci_fn')
    if result is None:
        result = cg_fn() | ch_fn() 
        precalc['ci_fn'] = result
    return result


def la_fn():
    result = precalc.get('la_fn')
    if result is None:
        result = 1 & kz_fn() 
        precalc['la_fn'] = result
    return result


def gg_fn():
    result = precalc.get('gg_fn')
    if result is None:
        result = gf_fn() | ge_fn() 
        precalc['gg_fn'] = result
    return result


def gk_fn():
    result = precalc.get('gk_fn')
    if result is None:
        result = gj_fn() >> 2 
        precalc['gk_fn'] = result
    return result


def de_fn():
    result = precalc.get('de_fn')
    if result is None:
        result = dd_fn() >> 2 
        precalc['de_fn'] = result
    return result


def lt_fn():
    result = precalc.get('lt_fn')
    if result is None:
        result = ~ ls_fn() 
        precalc['lt_fn'] = result
    return result


def lj_fn():
    result = precalc.get('lj_fn')
    if result is None:
        result = lh_fn() | li_fn() 
        precalc['lj_fn'] = result
    return result


def jt_fn():
    result = precalc.get('jt_fn')
    if result is None:
        result = jr_fn() | js_fn() 
        precalc['jt_fn'] = result
    return result


def ax_fn():
    result = precalc.get('ax_fn')
    if result is None:
        result = au_fn() & av_fn() 
        precalc['ax_fn'] = result
    return result


def c_fn():
    result = precalc.get('c_fn')
    if result is None:
        result = 0 
        precalc['c_fn'] = result
    return result


def hr_fn():
    result = precalc.get('hr_fn')
    if result is None:
        result = he_fn() & hp_fn() 
        precalc['hr_fn'] = result
    return result


def ig_fn():
    result = precalc.get('ig_fn')
    if result is None:
        result = id_fn() & if_fn() 
        precalc['ig_fn'] = result
    return result


def ew_fn():
    result = precalc.get('ew_fn')
    if result is None:
        result = et_fn() >> 5 
        precalc['ew_fn'] = result
    return result


def bs_fn():
    result = precalc.get('bs_fn')
    if result is None:
        result = bp_fn() & bq_fn() 
        precalc['bs_fn'] = result
    return result


def h_fn():
    result = precalc.get('h_fn')
    if result is None:
        result = e_fn() & f_fn() 
        precalc['h_fn'] = result
    return result


def ma_fn():
    result = precalc.get('ma_fn')
    if result is None:
        result = ly_fn() | lz_fn() 
        precalc['ma_fn'] = result
    return result


def lv_fn():
    result = precalc.get('lv_fn')
    if result is None:
        result = 1 & lu_fn() 
        precalc['lv_fn'] = result
    return result


def je_fn():
    result = precalc.get('je_fn')
    if result is None:
        result = ~ jd_fn() 
        precalc['je_fn'] = result
    return result


def hb_fn():
    result = precalc.get('hb_fn')
    if result is None:
        result = ha_fn() | gz_fn() 
        precalc['hb_fn'] = result
    return result


def er_fn():
    result = precalc.get('er_fn')
    if result is None:
        result = dy_fn() >> 1 
        precalc['er_fn'] = result
    return result


def iv_fn():
    result = precalc.get('iv_fn')
    if result is None:
        result = iu_fn() >> 2 
        precalc['iv_fn'] = result
    return result


def hs_fn():
    result = precalc.get('hs_fn')
    if result is None:
        result = ~ hr_fn() 
        precalc['hs_fn'] = result
    return result


def bl_fn():
    result = precalc.get('bl_fn')
    if result is None:
        result = as_fn() >> 1 
        precalc['bl_fn'] = result
    return result


def kl_fn():
    result = precalc.get('kl_fn')
    if result is None:
        result = kk_fn() >> 2 
        precalc['kl_fn'] = result
    return result


def p_fn():
    result = precalc.get('p_fn')
    if result is None:
        result = b_fn() & n_fn() 
        precalc['p_fn'] = result
    return result


def lq_fn():
    result = precalc.get('lq_fn')
    if result is None:
        result = ln_fn() & lp_fn() 
        precalc['lq_fn'] = result
    return result


def cr_fn():
    result = precalc.get('cr_fn')
    if result is None:
        result = cj_fn() & cp_fn() 
        precalc['cr_fn'] = result
    return result


def do_fn():
    result = precalc.get('do_fn')
    if result is None:
        result = dl_fn() & dn_fn() 
        precalc['do_fn'] = result
    return result


def cj_fn():
    result = precalc.get('cj_fn')
    if result is None:
        result = ci_fn() >> 2 
        precalc['cj_fn'] = result
    return result


def be_fn():
    result = precalc.get('be_fn')
    if result is None:
        result = as_fn() | bd_fn() 
        precalc['be_fn'] = result
    return result


def gi_fn():
    result = precalc.get('gi_fn')
    if result is None:
        result = ge_fn() << 15 
        precalc['gi_fn'] = result
    return result


def ic_fn():
    result = precalc.get('ic_fn')
    if result is None:
        result = hz_fn() >> 5 
        precalc['ic_fn'] = result
    return result


def ep_fn():
    result = precalc.get('ep_fn')
    if result is None:
        result = dv_fn() << 1 
        precalc['ep_fn'] = result
    return result


def ks_fn():
    result = precalc.get('ks_fn')
    if result is None:
        result = kl_fn() | kr_fn() 
        precalc['ks_fn'] = result
    return result


def gv_fn():
    result = precalc.get('gv_fn')
    if result is None:
        result = gj_fn() | gu_fn() 
        precalc['gv_fn'] = result
    return result


def hh_fn():
    result = precalc.get('hh_fn')
    if result is None:
        result = he_fn() >> 5 
        precalc['hh_fn'] = result
    return result


def fh_fn():
    result = precalc.get('fh_fn')
    if result is None:
        result = ~ fg_fn() 
        precalc['fh_fn'] = result
    return result


def hj_fn():
    result = precalc.get('hj_fn')
    if result is None:
        result = hg_fn() & hh_fn() 
        precalc['hj_fn'] = result
    return result


def o_fn():
    result = precalc.get('o_fn')
    if result is None:
        result = b_fn() | n_fn() 
        precalc['o_fn'] = result
    return result


def jo_fn():
    result = precalc.get('jo_fn')
    if result is None:
        result = jk_fn() << 15 
        precalc['jo_fn'] = result
    return result


def hd_fn():
    result = precalc.get('hd_fn')
    if result is None:
        result = gz_fn() << 15 
        precalc['hd_fn'] = result
    return result


def dc_fn():
    result = precalc.get('dc_fn')
    if result is None:
        result = cy_fn() << 15 
        precalc['dc_fn'] = result
    return result


def kn_fn():
    result = precalc.get('kn_fn')
    if result is None:
        result = kk_fn() >> 5 
        precalc['kn_fn'] = result
    return result


def ck_fn():
    result = precalc.get('ck_fn')
    if result is None:
        result = ci_fn() >> 3 
        precalc['ck_fn'] = result
    return result


def ba_fn():
    result = precalc.get('ba_fn')
    if result is None:
        result = at_fn() | az_fn() 
        precalc['ba_fn'] = result
    return result


def iw_fn():
    result = precalc.get('iw_fn')
    if result is None:
        result = iu_fn() >> 3 
        precalc['iw_fn'] = result
    return result


def kr_fn():
    result = precalc.get('kr_fn')
    if result is None:
        result = ko_fn() & kq_fn() 
        precalc['kr_fn'] = result
    return result


def ei_fn():
    result = precalc.get('ei_fn')
    if result is None:
        result = ~ eh_fn() 
        precalc['ei_fn'] = result
    return result


def as_fn():
    result = precalc.get('as_fn')
    if result is None:
        result = aq_fn() | ar_fn() 
        precalc['as_fn'] = result
    return result


def jb_fn():
    result = precalc.get('jb_fn')
    if result is None:
        result = iy_fn() & ja_fn() 
        precalc['jb_fn'] = result
    return result


def df_fn():
    result = precalc.get('df_fn')
    if result is None:
        result = dd_fn() >> 3 
        precalc['df_fn'] = result
    return result


def bp_fn():
    result = precalc.get('bp_fn')
    if result is None:
        result = bn_fn() >> 3 
        precalc['bp_fn'] = result
    return result


def cd_fn():
    result = precalc.get('cd_fn')
    if result is None:
        result = 1 & cc_fn() 
        precalc['cd_fn'] = result
    return result


def bb_fn():
    result = precalc.get('bb_fn')
    if result is None:
        result = at_fn() & az_fn() 
        precalc['bb_fn'] = result
    return result


def aj_fn():
    result = precalc.get('aj_fn')
    if result is None:
        result = x_fn() | ai_fn() 
        precalc['aj_fn'] = result
    return result


def kx_fn():
    result = precalc.get('kx_fn')
    if result is None:
        result = kk_fn() & kv_fn() 
        precalc['kx_fn'] = result
    return result


def ap_fn():
    result = precalc.get('ap_fn')
    if result is None:
        result = ao_fn() | an_fn() 
        precalc['ap_fn'] = result
    return result


def ea_fn():
    result = precalc.get('ea_fn')
    if result is None:
        result = dy_fn() >> 3 
        precalc['ea_fn'] = result
    return result


def aq_fn():
    result = precalc.get('aq_fn')
    if result is None:
        result = x_fn() >> 1 
        precalc['aq_fn'] = result
    return result


def fc_fn():
    result = precalc.get('fc_fn')
    if result is None:
        result = eu_fn() & fa_fn() 
        precalc['fc_fn'] = result
    return result


def kt_fn():
    result = precalc.get('kt_fn')
    if result is None:
        result = kl_fn() & kr_fn() 
        precalc['kt_fn'] = result
    return result


def ii_fn():
    result = precalc.get('ii_fn')
    if result is None:
        result = ia_fn() & ig_fn() 
        precalc['ii_fn'] = result
    return result


def di_fn():
    result = precalc.get('di_fn')
    if result is None:
        result = df_fn() & dg_fn() 
        precalc['di_fn'] = result
    return result


def fy_fn():
    result = precalc.get('fy_fn')
    if result is None:
        result = ~ fx_fn() 
        precalc['fy_fn'] = result
    return result


def n_fn():
    result = precalc.get('n_fn')
    if result is None:
        result = k_fn() & m_fn() 
        precalc['n_fn'] = result
    return result


def bq_fn():
    result = precalc.get('bq_fn')
    if result is None:
        result = bn_fn() >> 5 
        precalc['bq_fn'] = result
    return result


def kp_fn():
    result = precalc.get('kp_fn')
    if result is None:
        result = km_fn() & kn_fn() 
        precalc['kp_fn'] = result
    return result


def dx_fn():
    result = precalc.get('dx_fn')
    if result is None:
        result = dt_fn() << 15 
        precalc['dx_fn'] = result
    return result


def ia_fn():
    result = precalc.get('ia_fn')
    if result is None:
        result = hz_fn() >> 2 
        precalc['ia_fn'] = result
    return result


def am_fn():
    result = precalc.get('am_fn')
    if result is None:
        result = aj_fn() & al_fn() 
        precalc['am_fn'] = result
    return result


def ch_fn():
    result = precalc.get('ch_fn')
    if result is None:
        result = cd_fn() << 15 
        precalc['ch_fn'] = result
    return result


def he_fn():
    result = precalc.get('he_fn')
    if result is None:
        result = hc_fn() | hd_fn() 
        precalc['he_fn'] = result
    return result


def hg_fn():
    result = precalc.get('hg_fn')
    if result is None:
        result = he_fn() >> 3 
        precalc['hg_fn'] = result
    return result


def bz_fn():
    result = precalc.get('bz_fn')
    if result is None:
        result = bn_fn() | by_fn() 
        precalc['bz_fn'] = result
    return result


def ku_fn():
    result = precalc.get('ku_fn')
    if result is None:
        result = ~ kt_fn() 
        precalc['ku_fn'] = result
    return result


def ac_fn():
    result = precalc.get('ac_fn')
    if result is None:
        result = z_fn() & aa_fn() 
        precalc['ac_fn'] = result
    return result


def al_fn():
    result = precalc.get('al_fn')
    if result is None:
        result = ~ ak_fn() 
        precalc['al_fn'] = result
    return result


def cx_fn():
    result = precalc.get('cx_fn')
    if result is None:
        result = cu_fn() & cw_fn() 
        precalc['cx_fn'] = result
    return result


def if_fn():
    result = precalc.get('if_fn')
    if result is None:
        result = ~ ie_fn() 
        precalc['if_fn'] = result
    return result


def dz_fn():
    result = precalc.get('dz_fn')
    if result is None:
        result = dy_fn() >> 2 
        precalc['dz_fn'] = result
    return result


def it_fn():
    result = precalc.get('it_fn')
    if result is None:
        result = ip_fn() << 15 
        precalc['it_fn'] = result
    return result


def dl_fn():
    result = precalc.get('dl_fn')
    if result is None:
        result = de_fn() | dk_fn() 
        precalc['dl_fn'] = result
    return result


def aw_fn():
    result = precalc.get('aw_fn')
    if result is None:
        result = au_fn() | av_fn() 
        precalc['aw_fn'] = result
    return result


def jj_fn():
    result = precalc.get('jj_fn')
    if result is None:
        result = jg_fn() & ji_fn() 
        precalc['jj_fn'] = result
    return result


def cv_fn():
    result = precalc.get('cv_fn')
    if result is None:
        result = ci_fn() & ct_fn() 
        precalc['cv_fn'] = result
    return result


def eb_fn():
    result = precalc.get('eb_fn')
    if result is None:
        result = dy_fn() >> 5 
        precalc['eb_fn'] = result
    return result


def hz_fn():
    result = precalc.get('hz_fn')
    if result is None:
        result = hx_fn() | hy_fn() 
        precalc['hz_fn'] = result
    return result


def fb_fn():
    result = precalc.get('fb_fn')
    if result is None:
        result = eu_fn() | fa_fn() 
        precalc['fb_fn'] = result
    return result


def gl_fn():
    result = precalc.get('gl_fn')
    if result is None:
        result = gj_fn() >> 3 
        precalc['gl_fn'] = result
    return result


def gb_fn():
    result = precalc.get('gb_fn')
    if result is None:
        result = fo_fn() & fz_fn() 
        precalc['gb_fn'] = result
    return result


def jk_fn():
    result = precalc.get('jk_fn')
    if result is None:
        result = 1 & jj_fn() 
        precalc['jk_fn'] = result
    return result


def kb_fn():
    result = precalc.get('kb_fn')
    if result is None:
        result = jp_fn() | ka_fn() 
        precalc['kb_fn'] = result
    return result


def dm_fn():
    result = precalc.get('dm_fn')
    if result is None:
        result = de_fn() & dk_fn() 
        precalc['dm_fn'] = result
    return result


def fa_fn():
    result = precalc.get('fa_fn')
    if result is None:
        result = ex_fn() & ez_fn() 
        precalc['fa_fn'] = result
    return result


def dh_fn():
    result = precalc.get('dh_fn')
    if result is None:
        result = df_fn() | dg_fn() 
        precalc['dh_fn'] = result
    return result


def jc_fn():
    result = precalc.get('jc_fn')
    if result is None:
        result = iv_fn() | jb_fn() 
        precalc['jc_fn'] = result
    return result


def aa_fn():
    result = precalc.get('aa_fn')
    if result is None:
        result = x_fn() >> 5 
        precalc['aa_fn'] = result
    return result


def hk_fn():
    result = precalc.get('hk_fn')
    if result is None:
        result = ~ hj_fn() 
        precalc['hk_fn'] = result
    return result


def in_fn():
    result = precalc.get('in_fn')
    if result is None:
        result = ~ im_fn() 
        precalc['in_fn'] = result
    return result


def gf_fn():
    result = precalc.get('gf_fn')
    if result is None:
        result = fl_fn() << 1 
        precalc['gf_fn'] = result
    return result


def hy_fn():
    result = precalc.get('hy_fn')
    if result is None:
        result = hu_fn() << 15 
        precalc['hy_fn'] = result
    return result


def ir_fn():
    result = precalc.get('ir_fn')
    if result is None:
        result = iq_fn() | ip_fn() 
        precalc['ir_fn'] = result
    return result


def ix_fn():
    result = precalc.get('ix_fn')
    if result is None:
        result = iu_fn() >> 5 
        precalc['ix_fn'] = result
    return result


def fd_fn():
    result = precalc.get('fd_fn')
    if result is None:
        result = ~ fc_fn() 
        precalc['fd_fn'] = result
    return result


def em_fn():
    result = precalc.get('em_fn')
    if result is None:
        result = ~ el_fn() 
        precalc['em_fn'] = result
    return result


def cm_fn():
    result = precalc.get('cm_fn')
    if result is None:
        result = ck_fn() | cl_fn() 
        precalc['cm_fn'] = result
    return result


def ev_fn():
    result = precalc.get('ev_fn')
    if result is None:
        result = et_fn() >> 3 
        precalc['ev_fn'] = result
    return result


def iq_fn():
    result = precalc.get('iq_fn')
    if result is None:
        result = hw_fn() << 1 
        precalc['iq_fn'] = result
    return result


def cl_fn():
    result = precalc.get('cl_fn')
    if result is None:
        result = ci_fn() >> 5 
        precalc['cl_fn'] = result
    return result


def jd_fn():
    result = precalc.get('jd_fn')
    if result is None:
        result = iv_fn() & jb_fn() 
        precalc['jd_fn'] = result
    return result


def dg_fn():
    result = precalc.get('dg_fn')
    if result is None:
        result = dd_fn() >> 5 
        precalc['dg_fn'] = result
    return result


def at_fn():
    result = precalc.get('at_fn')
    if result is None:
        result = as_fn() >> 2 
        precalc['at_fn'] = result
    return result


def jz_fn():
    result = precalc.get('jz_fn')
    if result is None:
        result = ~ jy_fn() 
        precalc['jz_fn'] = result
    return result


def ai_fn():
    result = precalc.get('ai_fn')
    if result is None:
        result = af_fn() & ah_fn() 
        precalc['ai_fn'] = result
    return result


def dt_fn():
    result = precalc.get('dt_fn')
    if result is None:
        result = 1 & ds_fn() 
        precalc['dt_fn'] = result
    return result


def ka_fn():
    result = precalc.get('ka_fn')
    if result is None:
        result = jx_fn() & jz_fn() 
        precalc['ka_fn'] = result
    return result


def du_fn():
    result = precalc.get('du_fn')
    if result is None:
        result = da_fn() << 1 
        precalc['du_fn'] = result
    return result


def fv_fn():
    result = precalc.get('fv_fn')
    if result is None:
        result = fs_fn() & fu_fn() 
        precalc['fv_fn'] = result
    return result


def ki_fn():
    result = precalc.get('ki_fn')
    if result is None:
        result = jp_fn() >> 1 
        precalc['ki_fn'] = result
    return result


def iz_fn():
    result = precalc.get('iz_fn')
    if result is None:
        result = iw_fn() & ix_fn() 
        precalc['iz_fn'] = result
    return result


def iy_fn():
    result = precalc.get('iy_fn')
    if result is None:
        result = iw_fn() | ix_fn() 
        precalc['iy_fn'] = result
    return result


def es_fn():
    result = precalc.get('es_fn')
    if result is None:
        result = eo_fn() << 15 
        precalc['es_fn'] = result
    return result


def ey_fn():
    result = precalc.get('ey_fn')
    if result is None:
        result = ev_fn() & ew_fn() 
        precalc['ey_fn'] = result
    return result


def bd_fn():
    result = precalc.get('bd_fn')
    if result is None:
        result = ba_fn() & bc_fn() 
        precalc['bd_fn'] = result
    return result


def fx_fn():
    result = precalc.get('fx_fn')
    if result is None:
        result = fp_fn() & fv_fn() 
        precalc['fx_fn'] = result
    return result


def jf_fn():
    result = precalc.get('jf_fn')
    if result is None:
        result = jc_fn() & je_fn() 
        precalc['jf_fn'] = result
    return result


def eu_fn():
    result = precalc.get('eu_fn')
    if result is None:
        result = et_fn() >> 2 
        precalc['eu_fn'] = result
    return result


def kh_fn():
    result = precalc.get('kh_fn')
    if result is None:
        result = kg_fn() | kf_fn() 
        precalc['kh_fn'] = result
    return result


def jg_fn():
    result = precalc.get('jg_fn')
    if result is None:
        result = iu_fn() | jf_fn() 
        precalc['jg_fn'] = result
    return result


def et_fn():
    result = precalc.get('et_fn')
    if result is None:
        result = er_fn() | es_fn() 
        precalc['et_fn'] = result
    return result


def fp_fn():
    result = precalc.get('fp_fn')
    if result is None:
        result = fo_fn() >> 2 
        precalc['fp_fn'] = result
    return result


def cb_fn():
    result = precalc.get('cb_fn')
    if result is None:
        result = ~ ca_fn() 
        precalc['cb_fn'] = result
    return result


def by_fn():
    result = precalc.get('by_fn')
    if result is None:
        result = bv_fn() & bx_fn() 
        precalc['by_fn'] = result
    return result


def ao_fn():
    result = precalc.get('ao_fn')
    if result is None:
        result = u_fn() << 1 
        precalc['ao_fn'] = result
    return result


def cp_fn():
    result = precalc.get('cp_fn')
    if result is None:
        result = cm_fn() & co_fn() 
        precalc['cp_fn'] = result
    return result


def af_fn():
    result = precalc.get('af_fn')
    if result is None:
        result = y_fn() | ae_fn() 
        precalc['af_fn'] = result
    return result


def ca_fn():
    result = precalc.get('ca_fn')
    if result is None:
        result = bn_fn() & by_fn() 
        precalc['ca_fn'] = result
    return result


def kf_fn():
    result = precalc.get('kf_fn')
    if result is None:
        result = 1 & ke_fn() 
        precalc['kf_fn'] = result
    return result


def jw_fn():
    result = precalc.get('jw_fn')
    if result is None:
        result = jt_fn() & jv_fn() 
        precalc['jw_fn'] = result
    return result


def fs_fn():
    result = precalc.get('fs_fn')
    if result is None:
        result = fq_fn() | fr_fn() 
        precalc['fs_fn'] = result
    return result


def el_fn():
    result = precalc.get('el_fn')
    if result is None:
        result = dy_fn() & ej_fn() 
        precalc['el_fn'] = result
    return result


def kd_fn():
    result = precalc.get('kd_fn')
    if result is None:
        result = ~ kc_fn() 
        precalc['kd_fn'] = result
    return result


def ex_fn():
    result = precalc.get('ex_fn')
    if result is None:
        result = ev_fn() | ew_fn() 
        precalc['ex_fn'] = result
    return result


def dp_fn():
    result = precalc.get('dp_fn')
    if result is None:
        result = dd_fn() | do_fn() 
        precalc['dp_fn'] = result
    return result


def cw_fn():
    result = precalc.get('cw_fn')
    if result is None:
        result = ~ cv_fn() 
        precalc['cw_fn'] = result
    return result


def gu_fn():
    result = precalc.get('gu_fn')
    if result is None:
        result = gr_fn() & gt_fn() 
        precalc['gu_fn'] = result
    return result


def dw_fn():
    result = precalc.get('dw_fn')
    if result is None:
        result = dd_fn() >> 1 
        precalc['dw_fn'] = result
    return result


def gx_fn():
    result = precalc.get('gx_fn')
    if result is None:
        result = ~ gw_fn() 
        precalc['gx_fn'] = result
    return result


def ja_fn():
    result = precalc.get('ja_fn')
    if result is None:
        result = ~ iz_fn() 
        precalc['ja_fn'] = result
    return result


def ip_fn():
    result = precalc.get('ip_fn')
    if result is None:
        result = 1 & io_fn() 
        precalc['ip_fn'] = result
    return result


def ah_fn():
    result = precalc.get('ah_fn')
    if result is None:
        result = ~ ag_fn() 
        precalc['ah_fn'] = result
    return result


def f_fn():
    result = precalc.get('f_fn')
    if result is None:
        result = b_fn() >> 5 
        precalc['f_fn'] = result
    return result


def cs_fn():
    result = precalc.get('cs_fn')
    if result is None:
        result = ~ cr_fn() 
        precalc['cs_fn'] = result
    return result


def ke_fn():
    result = precalc.get('ke_fn')
    if result is None:
        result = kb_fn() & kd_fn() 
        precalc['ke_fn'] = result
    return result


def ju_fn():
    result = precalc.get('ju_fn')
    if result is None:
        result = jr_fn() & js_fn() 
        precalc['ju_fn'] = result
    return result


def ct_fn():
    result = precalc.get('ct_fn')
    if result is None:
        result = cq_fn() & cs_fn() 
        precalc['ct_fn'] = result
    return result


def io_fn():
    result = precalc.get('io_fn')
    if result is None:
        result = il_fn() & in_fn() 
        precalc['io_fn'] = result
    return result


def jv_fn():
    result = precalc.get('jv_fn')
    if result is None:
        result = ~ ju_fn() 
        precalc['jv_fn'] = result
    return result


def dv_fn():
    result = precalc.get('dv_fn')
    if result is None:
        result = du_fn() | dt_fn() 
        precalc['dv_fn'] = result
    return result


def dq_fn():
    result = precalc.get('dq_fn')
    if result is None:
        result = dd_fn() & do_fn() 
        precalc['dq_fn'] = result
    return result


def d_fn():
    result = precalc.get('d_fn')
    if result is None:
        result = b_fn() >> 2 
        precalc['d_fn'] = result
    return result


def kg_fn():
    result = precalc.get('kg_fn')
    if result is None:
        result = jm_fn() << 1 
        precalc['kg_fn'] = result
    return result


def dr_fn():
    result = precalc.get('dr_fn')
    if result is None:
        result = ~ dq_fn() 
        precalc['dr_fn'] = result
    return result


def bv_fn():
    result = precalc.get('bv_fn')
    if result is None:
        result = bo_fn() | bu_fn() 
        precalc['bv_fn'] = result
    return result


def gr_fn():
    result = precalc.get('gr_fn')
    if result is None:
        result = gk_fn() | gq_fn() 
        precalc['gr_fn'] = result
    return result


def hq_fn():
    result = precalc.get('hq_fn')
    if result is None:
        result = he_fn() | hp_fn() 
        precalc['hq_fn'] = result
    return result


def i_fn():
    result = precalc.get('i_fn')
    if result is None:
        result = ~ h_fn() 
        precalc['i_fn'] = result
    return result


def hn_fn():
    result = precalc.get('hn_fn')
    if result is None:
        result = hf_fn() & hl_fn() 
        precalc['hn_fn'] = result
    return result


def gy_fn():
    result = precalc.get('gy_fn')
    if result is None:
        result = gv_fn() & gx_fn() 
        precalc['gy_fn'] = result
    return result


def ak_fn():
    result = precalc.get('ak_fn')
    if result is None:
        result = x_fn() & ai_fn() 
        precalc['ak_fn'] = result
    return result


def bw_fn():
    result = precalc.get('bw_fn')
    if result is None:
        result = bo_fn() & bu_fn() 
        precalc['bw_fn'] = result
    return result


def ht_fn():
    result = precalc.get('ht_fn')
    if result is None:
        result = hq_fn() & hs_fn() 
        precalc['ht_fn'] = result
    return result


def is_fn():
    result = precalc.get('is_fn')
    if result is None:
        result = hz_fn() >> 1 
        precalc['is_fn'] = result
    return result


def gm_fn():
    result = precalc.get('gm_fn')
    if result is None:
        result = gj_fn() >> 5 
        precalc['gm_fn'] = result
    return result


def j_fn():
    result = precalc.get('j_fn')
    if result is None:
        result = g_fn() & i_fn() 
        precalc['j_fn'] = result
    return result


def gs_fn():
    result = precalc.get('gs_fn')
    if result is None:
        result = gk_fn() & gq_fn() 
        precalc['gs_fn'] = result
    return result


def ds_fn():
    result = precalc.get('ds_fn')
    if result is None:
        result = dp_fn() & dr_fn() 
        precalc['ds_fn'] = result
    return result


def e_fn():
    result = precalc.get('e_fn')
    if result is None:
        result = b_fn() >> 3 
        precalc['e_fn'] = result
    return result


def go_fn():
    result = precalc.get('go_fn')
    if result is None:
        result = gl_fn() & gm_fn() 
        precalc['go_fn'] = result
    return result


def gn_fn():
    result = precalc.get('gn_fn')
    if result is None:
        result = gl_fn() | gm_fn() 
        precalc['gn_fn'] = result
    return result


def ag_fn():
    result = precalc.get('ag_fn')
    if result is None:
        result = y_fn() & ae_fn() 
        precalc['ag_fn'] = result
    return result


def hw_fn():
    result = precalc.get('hw_fn')
    if result is None:
        result = hv_fn() | hu_fn() 
        precalc['hw_fn'] = result
    return result


def b_fn():
    return 46065
    result = precalc.get('b_fn')
    if result is None:
        result = 1674 
        precalc['b_fn'] = result
    return result


def ae_fn():
    result = precalc.get('ae_fn')
    if result is None:
        result = ab_fn() & ad_fn() 
        precalc['ae_fn'] = result
    return result


def ad_fn():
    result = precalc.get('ad_fn')
    if result is None:
        result = ~ ac_fn() 
        precalc['ad_fn'] = result
    return result


def hu_fn():
    result = precalc.get('hu_fn')
    if result is None:
        result = 1 & ht_fn() 
        precalc['hu_fn'] = result
    return result


def ho_fn():
    result = precalc.get('ho_fn')
    if result is None:
        result = ~ hn_fn() 
        precalc['ho_fn'] = result
    return result

print(a_fn())
