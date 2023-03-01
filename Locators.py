################### Login #########################

login_username="//*[@id='loginform']/div[1]/input[4]"
login_btn_submit_next="//*[@id='loginform']/div[2]/button"
login_password="//*[@id='codeform']/div[1]/input"
login_btn_submit="//*[@id='codeform']/div[2]/button"

################### Orders #########################

click_orders= "/html/body/div[1]/aside/section/ul/li[7]/a"
orders_start_date= "//*[@id='start-date']"
orders_start_date_back= "//*[@id='plotId']/div[1]/div[3]"
orders_start_date_month= "//*[@id='plotId']/div[1]/div[2]"
orders_start_date_month_option= "//*[@id='plotId']/div[2]/div/div[1]"
orders_start_date_option= "//*[@id='plotId']/div[2]/div/div/table/tbody/tr[1]/td[3]"
orders_end_date= "//*[@id='end-date']"
# orders_end_date_month= "//*[@id='plotId']/div[1]/div[2]"
orders_end_date_month= "/html/body/div[8]/div/div[1]/div[2]"
# orders_end_date_month_option= "//*[@id='plotId']/div[2]/div/div[1]"
orders_end_date_month_option= "/html/body/div[8]/div/div[2]/div/div[1]"
orders_end_date_back= "//*[@id='plotId']/div[1]/div[3]"
# orders_end_date_option= "//*[@id='plotId']/div[2]/div/div/table/tbody/tr[5]/td[5]"
orders_end_date_option= "/html/body/div[8]/div/div[2]/div/div/table/tbody/tr[5]/td[5]"
orders_click_span= "//*[@id='dateFilter']/div[2]/input"
# orders_dateFilter= "//*[@id='dateFilter']"
orders_dateFilter= "/html/body/div[1]/div[1]/section[2]/span[1]/div[2]/div/div/div/div/div/form/div[1]/button"
# orders_result= "//*[@id='table-753']/thead/tr[1]/th"
orders_result= "/html/body/div[1]/div[1]/section[2]/div[3]/div/div/div/table/thead/tr[1]"
orders_normalize_space= "//*[normalize-space(text())='نتایج 1 تا 30 از 1353 نتیجه']"

################### orders_create #########################

click_new_orders_create= "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[1]/a[1]"
click_orders_create="//*[@id='main-content-wrapper']/section[2]/a"
orders_create_name_select= "//*[@id='chooseservices']/form/div[1]/div/div/div[2]/div/div/span/span[1]"
orders_create_name_select_option= "//*[@id='select2-formuser_id_owner-n1-results']/li"
orders_create_name_select_option_text= "//*[@id='select2-formuser_id_owner-n1-container']"
orders_create_name_select_text= "/html/body/span/span/span[1]/input"
orders_create_check_transport= "//*[@id='transport']"
orders_create_check_clearance="//*[@id='clearance']"
orders_create_chooseservices="//*[@id='chooseservices']/form/div[2]/div/div/button"

################### orders_create_check #########################

orders_create_check_total_weight= "//*[@id='formtotalweight-n1']"
orders_create_check_total_v_weight= "//*[@id='formtotalvweight-n1']"
orders_create_check_total_c_weight= "//*[@id='formtotalcweight-n1']"
orders_create_check_total_price= "//*[@id='formtotalprice-n1']"
orders_create_check_price_unit= "//*[@id='formpriceunit-n1']"

################### Completion_of_information #########################

orders_create_information_type="//*[@id='formorder_type-n1']"
orders_create_information_type_option="//*[@id='formorder_type-n1']/option[1]"
orders_create_information_transport="//*[@id='formtransport_type-n1']"
orders_create_information_transport_option="//*[@id='formtransport_type-n1']/option[1]"
orders_create_information_senders="//*[@id='formsenders_count-n1']"
orders_create_information_must_pay_before_transport="//*[@id='formmustpaybeforetransport-n1']"
orders_create_information_must_pay_before_transport_option="//*[@id='formmustpaybeforetransport-n1']/option[1]"
orders_create_information_description="//*[@id='formsenders_description-n1']"
orders_create_information_pay_in_china="//*[@id='formpay_in_china-n1']"
orders_create_information_pay_in_china_option="//*[@id='formpay_in_china-n1']/option[1]"
orders_create_information_area_one="//*[@id='formis_areaone-n1']"

################### information_sender #########################

orders_create_information_sender_city_btn="//*[@id='information']/div/div/form/div[2]/div[2]/div[2]/div/a[1]"
orders_create_information_sender_city="//*[@id='information']/div/div/form/div[2]/div[2]/div[1]/div/div/span"
orders_create_information_sender_city_check_name="//*[@id='select2-formsender_city-n1-container']"
# orders_create_information_sender_city_check_name="//*[@id='information']/div/div/form/div[2]/div[2]/div[1]/div/div"
orders_create_information_sender_city_name="/html/body/span/span/span[1]/input"
orders_create_information_sender_city_option="//*[@id='select2-formsender_city-n1-results']/li"
orders_create_information_sender_name_select="//*[@id='select2-formsender_p-n1-container']"
orders_create_information_sender_name="/html/body/span/span/span[1]/input"
orders_create_information_sender_name_option="//*[@id='select2-formsender_p-n1-results']/li"
orders_create_information_sender_add="//*[@id='information']/div/div/form/div[2]/div[3]/div[1]/button"
orders_create_information_sender_new_persons="//*[@id='information']/div/div/form/div[2]/div[3]/div[1]/div[3]/a"
orders_create_information_sender_company="//*[@id='information']/div/div/form/div[2]/div[3]/div[3]/div[1]/span/span[1]/span"
orders_create_information_sender_company_add="//*[@id='information']/div/div/form/div[2]/div[3]/div[3]/button"
orders_create_information_sender_new_company="//*[@id='information']/div/div/form/div[2]/div[3]/div[3]/div[3]/a"

################### information_receiver #########################

orders_create_information_receiver_city="//*[@id='information']/div/div/form/div[3]/div[3]/div[1]/div/div/span"
orders_create_information_receiver_city_btn="//*[@id='information']/div/div/form/div[3]/div[3]/div[2]/div/a[1]"
# orders_create_information_receiver_city="//*[@id='information']/div/div/form/div[3]/div[3]/div[2]/div/a[1]"
orders_create_information_receiver_city_name="/html/body/span/span/span[1]/input"
orders_create_information_receiver_city_check_name="//*[@id='select2-formreceiver_city-n1-container']"
orders_create_information_receiver_city_option="//*[@id='select2-formreceiver_city-n1-results']/li"
orders_create_information_receiver_name_select="//*[@id='select2-formreceiver_p-n1-container']"
# orders_create_information_receiver_name_select="/html/body/div[1]/div/section[2]/div/div/div/div/div/div/div/form/div[3]/div[4]/div[1]/div[1]/div/div/span/span[1]/span/span[1]"
orders_create_information_receiver_name="/html/body/span/span/span[1]/input"
orders_create_information_receiver_option="//*[@id='select2-formreceiver_p-n1-results']/li"
orders_create_information_receiver_new_persons="//*[@id='information']/div/div/form/div[3]/div[4]/div[1]/div[3]/a"
orders_create_information_receiver_company="//*[@id='information']/div/div/form/div[2]/div[3]/div[3]/div[1]/span/span[1]/span"
orders_create_information_receiver_new_company="//*[@id='information']/div/div/form/div[3]/div[4]/div[2]/div[3]/a"

################### factor #########################

orders_create_information_sub_bill="//*[@id='formsubbill-n1']"
orders_create_information_sub_bill_option="//*[@id='formsubbill-n1']/option[1]"
orders_create_information_factor_rasmi_transport="//*[@id='formfactorrasmi_transport-n1']"
orders_create_information_factor_rasmi_transport_option="//*[@id='formfactorrasmi_transport-n1']/option[2]"
orders_create_information_factor_rasmi_clearance="//*[@id='formfactorrasmi_clearance-n1']"
orders_create_information_factor_rasmi_clearance_option="//*[@id='formfactorrasmi_clearance-n1']/option[2]"
orders_create_information_need_clearance_inquery="//*[@id='formneed_clearance_inquery-n1']"
orders_create_information_need_clearance_inquery_option="//*[@id='formneed_clearance_inquery-n1']/option[1]"
orders_create_information_clearance_youan_invoice_request="//*[@id='formclearance_youan_invoice_request-n1']"
orders_create_information_clearance_youan_invoice_request_option="//*[@id='formclearance_youan_invoice_request-n1']/option[2]"
orders_create_information_factor_rasmi="//*[@id='formfactorrasmi-n1']"
orders_create_information_factor_rasmi_option="//*[@id='formfactorrasmi-n1']/option[2]"
orders_create_information_invoice_to_container="//*[@id='select2-forminvoiceto_p-n1-container']"
orders_create_information_invoice_to_container_name="/html/body/span/span/span[1]/input"
orders_create_information_invoice_to_container_option="//*[@id='select2-forminvoiceto_p-n1-results']/li"
orders_create_information_goback="//*[@id='information']/div/div/form/div[6]/div[2]/button"
orders_create_information_approve="//*[@id='information']/div/div/form/div[6]/div[1]/button"
orders_create_information_factor_new_persons="//*[@id='information']/div/div/form/div[5]/div[3]/div[1]/a"
orders_create_information_factor_company="//*[@id='select2-forminvoiceto_c-n1-container']"
orders_create_information_factor_new_company="//*[@id='information']/div/div/form/div[5]/div[3]/div[3]/a"

################### review #########################

orders_create_next_review="//*[@id='review']/div/div/form/div[34]/div[1]/button"

################### check_the_order #########################

click_checking_the_order="//*[@id='main-content-wrapper']/section[2]/div[4]/a"
check_the_order_approved="//*[@id='boxConfirmOrder']/div/div[2]/form/button"

################### clearance_inquiry #########################

click_clearance_inquiry="//*[@id='main-content-wrapper']/section[1]/div[2]/div[6]/a"
clearance_inquiry_cargo_clearance="//*[@id='boxclearanceinqueryForm']/div/div[4]/div/div/span"
clearance_inquiry_cargo_clearance_option="//*[@id='select2-formagent-results']/li[1]"
clearance_inquiry_type="//*[@id='formclearance_type']"
clearance_inquiry_type_option="//*[@id='formclearance_type']/option[1]"
clearance_inquiry_Price="//*[@id='formprice']"
clearance_inquiry_Price_unit="//*[@id='formpriceunit']"
clearance_inquiry_comment="//*[@id='formcomment']"
clearance_inquiry_form_save="//*[@id='boxclearanceinqueryForm']/button"

################### other_inquiries #########################

click_other_inquiries="//*[@id='main-content-wrapper']/section[1]/div[2]/div[7]/a"
other_inquiries_services_invoice_type="//*[@id='formfactorrasmi']"
other_inquiries_services_invoice_type_option="//*[@id='formfactorrasmi']/option[2]"
other_inquiries_services_invoice_type_update="//*[@id='formotherinquery_type']"
other_inquiries_pre_factor_type="//*[@id='formotherinquery_type']/option[2]"
other_inquiries_price="//*[@id='formprice']"
other_inquiries_price_unit="//*[@id='formpriceunit']"
other_inquiries_price_unit_option="//*[@id='formpriceunit']/option[1]"
other_inquiries_description="//*[@id='formtext']"
other_inquiries_save_submit="//*[@id='fastinvoice']/div/div[2]/form/button"

################### persons #########################

click_persons="/html/body/div[1]/aside/section/ul/li[11]/a"
click_persons_financial="/html/body/div[1]/aside/section/ul/li[9]/a"

################### persons_create #########################

click_persons_create="//*[@id='main-content-wrapper']/section[2]/a[1]"
persons_create_check="//*[@id='main-content-wrapper']/section[1]/h1"
persons_create_firstname="//*[@id='formfirstname']"
persons_create_lastname="//*[@id='formlastname']"
persons_create_firstname_en="//*[@id='formfirstname_en']"
persons_create_lastname_en="//*[@id='formlastname_en']"
persons_create_gender="//*[@id='formgender']"
persons_create_gender_option="//*[@id='formgender']/option[2]"
persons_create_email="//*[@id='formemail']"
persons_create_non_iranian_nationals="//*[@id='formnon_iranian_nationals']"
persons_create_non_iranian_nationals_option="//*[@id='formnon_iranian_nationals']/option[1]"
persons_create_non_iranian_nationals_option2="//*[@id='formnon_iranian_nationals']/option[2]"
persons_create_code_melli="//*[@id='formcodemelli']"
persons_create_non_iranian_create_code_melli="//*[@id='formnon_iranian_nationals_code']"
persons_create_phone_number="//*[@id='formmobile1']"
persons_create_phone_number2="//*[@id='formmobile2']"
persons_create_phone1="//*[@id='formphone1']"
persons_create_phone2="//*[@id='formphone2']"
persons_create_internal_number="//*[@id='forminternal_number']"
persons_create_company_phone="//*[@id='formcompany_phone']"
persons_create_company_name="//*[@id='formcompany_name']"
persons_create_postalcode="//*[@id='formpostalcode']"
persons_create_address="//*[@id='formaddress']"
persons_create_agency="//*[@id='form-person']/div[19]/div/div/span"
persons_create_agency_option="//*[@id='select2-formagency_id-results']/li[1]"
persons_create_expert_user="//*[@id='form-person']/div[21]/div/div/span"
persons_create_expert_user_name="/html/body/span/span/span[1]/input"
persons_create_expert_user_option="//*[@id='select2-formexpert_user_id-results']/li[1]"
persons_create_how_find_us="//*[@id='formhow_find_us']"
persons_create_how_find_us_option="//*[@id='formhow_find_us']/option[2]"
persons_create_marketer="//*[@id='form-person']/div[23]/div/div/span"
persons_create_marketer_name="/html/body/span/span/span[1]/input"
persons_create_marketer_option="//*[@id='select2-formmarketer_id-results']/li[2]"
persons_create_description="//*[@id='formtext']"
persons_create_submit_btn="//*[@id='form-person']/div[30]/div/button"

################### persons_create_check #########################

persons_create_check_name="//*[@id='main-content-wrapper']/section[2]/div[1]/div/div[1]/div/div[1]/div[1]/div/div[1]/h3"
persons_create_check_expert_user="//*[@id='main-content-wrapper']/section[2]/div[1]/div/div[1]/div/div[3]/div/div[1]/div/h5"
persons_create_check_marketer="//*[@id='main-content-wrapper']/section[2]/div[1]/div/div[1]/div/div[3]/div/div[2]/div/h5"
persons_create_check_code_melli="//*[@id='main-content-wrapper']/section[2]/div[1]/div/div[1]/div/div[3]/div/div[3]/div/h5"
persons_create_check_agency="//*[@id='main-content-wrapper']/section[2]/div[1]/div/div[1]/div/div[3]/div/div[4]/div/h5"
persons_create_check_phone="//*[@id='main-content-wrapper']/section[2]/div[1]/div/div[1]/div/div[3]/div/div[5]/div/h5"
persons_create_check_phone_number="//*[@id='main-content-wrapper']/section[2]/div[1]/div/div[1]/div/div[3]/div/div[6]/div/h5"
persons_create_check_arian="//*[text()=' انتقال کاربر به آرین ']"
persons_create_check_connecting="//*[@href='http://testbpm.2ms.ir/persons/view/15489?createuser=1']"
persons_create_check_selection="//span[@class='selection']"
persons_create_check_input="//input[@type='text']"
persons_create_check_text="//input[@type='text']"
persons_create_check_select="//select"
persons_create_connected_user="//*[@id='main-content-wrapper']/section[2]/div[1]/div/div[1]/div/div[1]/div[1]/div/div[2]/div/a[3]"

persons_create_user_transactions="//*[@id='main-content-wrapper']/section[2]/div[2]/div/div[2]/div/div[1]"
persons_create_user_payments="//*[@id='main-content-wrapper']/section[2]/div[2]/div/div[2]/div/div[2]"
persons_create_payment_documents_in_Arian="//*[@id='main-content-wrapper']/section[2]/div[2]/div/div[2]/div/div[3]"
persons_create_refund_requests="//*[@id='main-content-wrapper']/section[2]/div[2]/div/div[2]/div/div[4]"
persons_create_doing="//*[@id='main-content-wrapper']/section[2]/div[3]/div/div[2]/div/div[1]"
persons_create_just_downloaded="//*[@id='main-content-wrapper']/section[2]/div[3]/div/div[2]/div/div[2]"
persons_create_delivered_not_settled="//*[@id='main-content-wrapper']/section[2]/div[3]/div/div[2]/div/div[3]"
persons_create_delivered_and_settled="//*[@id='main-content-wrapper']/section[2]/div[3]/div/div[2]/div/div[4]"
persons_create_canceled="//*[@id='main-content-wrapper']/section[2]/div[3]/div/div[2]/div/div[5]"

persons_create_customer_indebtedness="//*[@id='main-content-wrapper']/section[2]/div[2]/div/div[2]/div/div[5]"
persons_create_subscribed="//*[@id='main-content-wrapper']/section[2]/div[3]/div/div[2]/div/div[6]"
persons_create_suspended="//*[@id='main-content-wrapper']/section[2]/div[3]/div/div[2]/div/div[7]"
persons_create_list_all="//*[@id='main-content-wrapper']/section[2]/div[3]/div/div[2]/div/div[8]"

persons_create_user_transactions1="//*[@id='main-content-wrapper']/section[2]/div[3]/div/div[2]/div/div[1]"
persons_create_user_payments1="//*[@id='main-content-wrapper']/section[2]/div[3]/div/div[2]/div/div[2]"
persons_create_payment_documents_in_Arian1="//*[@id='main-content-wrapper']/section[2]/div[3]/div/div[2]/div/div[3]"
persons_create_refund_requests1="//*[@id='main-content-wrapper']/section[2]/div[3]/div/div[2]/div/div[4]"
persons_create_doing1="//*[@id='main-content-wrapper']/section[2]/div[4]/div/div[2]/div/div[1]"
persons_create_just_downloaded1="//*[@id='main-content-wrapper']/section[2]/div[4]/div/div[2]/div/div[2]"
persons_create_delivered_not_settled1="//*[@id='main-content-wrapper']/section[2]/div[4]/div/div[2]/div/div[3]"
persons_create_delivered_and_settled1="//*[@id='main-content-wrapper']/section[2]/div[4]/div/div[2]/div/div[4]"
persons_create_canceled1="//*[@id='main-content-wrapper']/section[2]/div[4]/div/div[2]/div/div[5]"

persons_create_customer_indebtedness1="//*[@id='main-content-wrapper']/section[2]/div[3]/div/div[2]/div/div[5]"
persons_create_subscribed1="//*[@id='main-content-wrapper']/section[2]/div[4]/div/div[2]/div/div[6]"
persons_create_suspended1="//*[@id='main-content-wrapper']/section[2]/div[4]/div/div[2]/div/div[7]"
persons_create_list_all1="//*[@id='main-content-wrapper']/section[2]/div[4]/div/div[2]/div/div[8]"

################### search_financial #########################

psp_search_select="/html/body/div[1]/aside/section/div[2]/span[1]"
psp_search_select_name="/html/body/span/span/span[1]/input"
# psp_search_select_option="//*[@id='select2-gsbw-results']/li"
# psp_search_select_option="//*[@id='select2-2ex9-results']/li"
# psp_search_select_option="//*[text()='Zahra Omrani / زهرا عمرانی / 989125135808 💵']"
psp_search_select_option="//*[@class='select2-results__option select2-results__option--highlighted']"
# psp_search_select_option2="//*[text()='کاربر تست / user test']"
psp_search_show_financial="//*[@id='main-content-wrapper']/section[2]/div[1]/div/div[1]/div/div[1]/div[1]/div/div[2]/div/a[2]"

################### check_btn #########################

persons_create_check_user_integration="//*[@id='main-content-wrapper']/section[2]/div[1]/div/div[1]/div/div[1]/div[1]/div/div[2]/div/a[1]"
persons_create_check_login_to_user_account="//*[@id='main-content-wrapper']/section[2]/div[1]/div/div[1]/div/div[1]/div[1]/div/div[2]/div/a[2]"
persons_create_check_edit_user_information="//*[@id='main-content-wrapper']/section[2]/div[1]/div/div[1]/div/div[1]/div[1]/div/div[2]/div/a[3]"
persons_create_check_user_changes="//*[@id='main-content-wrapper']/section[2]/div[1]/div/div[1]/div/div[1]/div[1]/div/div[2]/div/a[4]"
persons_create_check_user_locations="//*[@id='main-content-wrapper']/section[2]/div[1]/div/div[1]/div/div[1]/div[1]/div/div[2]/div/a[5]"
persons_create_check_persons_information="//*[@id='main-content-wrapper']/section[2]/div[1]/div/div[1]/div/div[1]/div[1]/div/div[2]/div/a[6]"

persons_create_check_us_dollar="//*[@id='main-content-wrapper']/section[2]/div[2]/div/div/div/div/div[2]/div[2]/div[1]/h4/span"
persons_create_check_euro="//*[@id='main-content-wrapper']/section[2]/div[2]/div/div/div/div/div[3]/div[2]/div[1]/h4/span"
persons_create_check_chinese_yuan="//*[@id='main-content-wrapper']/section[2]/div[2]/div/div/div/div/div[4]/div[2]/div[1]/h4/span"
persons_create_check_uae_dirham="//*[@id='main-content-wrapper']/section[2]/div[2]/div/div/div/div/div[5]/div[2]/div[1]/h4/span"
persons_create_check_lear="//*[@id='main-content-wrapper']/section[2]/div[2]/div/div/div/div/div[6]/div[2]/div[1]/h4/span"
persons_create_check_syrian_lira="//*[@id='main-content-wrapper']/section[2]/div[2]/div/div/div/div/div[7]/div[2]/div[1]/h4/span"
persons_create_check_iranian_rial="//*[@id='main-content-wrapper']/section[2]/div[2]/div/div/div/div/div[8]/div[2]/div[1]/h4/span"
persons_create_check_rial="//*[@id='main-content-wrapper']/section[2]/div[2]/div/div/div/div/div[9]/div[2]/div[1]/h4/span"

persons_create_check_inventory="//*[@id='credit-show']/a/div"
persons_create_check_records="//*[@id='main-content-wrapper']/section[2]/div[2]/div/div[2]/div/div[2]/div[2]"
persons_create_check_new_contract="//*[@id='main-content-wrapper']/section[2]/div[2]/div/div[2]/div/div[1]/div/div/a"

################### create_order_product #########################

click_create_order_product="//*[@id='orderproductsholder']/div[3]/a"
orders_create_category_select="//span[@id='select2-formop_general_category-container']"
orders_create_category_select_option="//li[contains(text(),'کالای دیجیتال')]"
orders_create_detailed_classification_of_goods="//span[@id='select2-formop_partial_category-container']"
orders_create_detailed_classification_of_goods_option="//li[contains(text(),'دوربین')]"
orders_create_form_name="//*[@id='formname']"
orders_create_form_name_en="//*[@id='formname_en']"
orders_create_form_type="//*[@id='formop_type']"
orders_create_form_type_option="//*[@id='formop_type']/option[1]"
orders_create_form_quantity="//*[@id='formop_quantity']"
orders_create_form_quantity_option="//*[@id='formop_quantity']/option[2]"
orders_create_form_quantity_number="//*[@id='formquantity']"
orders_create_form_one_weight="//*[@id='formoneweight']"
orders_create_form_weight="//*[@id='formweight']"
orders_create_form_length="//*[@id='formlength']"
orders_create_form_width="//*[@id='formwidth']"
orders_create_form_height="//*[@id='formheight']"
orders_create_form_cbm="//*[@id='formcbm']"
orders_create_form_v_weight="//*[@id='formvweight']"
orders_create_form_quantity_in_box="//*[@id='formquantity_in_box']"
orders_create_form_price_unit="//*[@id='formpriceunit']"
orders_create_form_price_unit_option="//*[@id='formpriceunit']/option[1]"
orders_create_form_price_unit_option2="//*[@id='formpriceunit']/option[2]"
orders_create_form_one_price="//*[@id='formoneprice']"
orders_create_form_price="//*[@id='formprice']"
orders_create_HSCODE="//span[@id='select2-formhscode-container']"
orders_create_HSCODE_option="//li[contains(text(),'01012910: ـ ـ ـ اسب برای مسابقه')]"
orders_create_form_part_number="//*[@id='formpartnumber']"
orders_create_form_buy_url="//*[@id='formbuy_url']"
orders_create_form_text="//*[@id='formtext']"
orders_create_form_country="//*[@id='formcreate_country']"
orders_create_submit_information="/html/body/div[8]/div/div/div/section[2]/div/div/div/div/form/div[31]/div/button"
orders_edit_product="//*[@id='orderproduct301100']/td[26]/a"

################### create_order_product #########################

# create_order_product_check_input="//form[@action='http://testbpm.2ms.ir/orderproducts/create/45019?onlycontent=1']//following::input[@type='text']"
create_order_product_check_input="//div[@class='row op-modify-form']//following::input[@type='text']"
create_order_product_check_select="//div[@class='row op-modify-form']//following::select"

product_check_branch_representation="//*[@id='review']/div/div/form/div[2]/div/div"
product_check_required_services="//*[@id='review']/div/div/form/div[3]/div/div"
product_check_senders_city="//*[@id='review']/div/div/form/div[6]/div/div"
product_check_receivers_city="//*[@id='review']/div/div/form/div[9]/div/div"
product_check_transportation_invoice_type="//*[@id='review']/div/div/form/div[17]/div/div"
product_check_type_of_shipping="//*[@id='review']/div/div/form/div[19]/div/div"
product_check_clearance_invoice_type="//*[@id='review']/div/div/form/div[20]/div/div"
product_check_clearance_inquiry_required="//*[@id='review']/div/div/form/div[21]/div/div"
product_check_other_services_invoice_type="//*[@id='review']/div/div/form/div[23]/div/div"
product_check_total_actual_weight="//*[@id='review']/div/div/form/div[24]/div/div"
product_check_total_volumetric_weight="//*[@id='review']/div/div/form/div[25]/div/div"
product_check_total_chargeable_weight="//*[@id='review']/div/div/form/div[26]/div/div"
product_check_total_value="//*[@id='review']/div/div/form/div[27]/div/div"
product_check_unit_of_value="//*[@id='review']/div/div/form/div[28]/div/div"













