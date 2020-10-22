#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-taxize
Version  : 0.9.98
Release  : 39
URL      : https://cran.r-project.org/src/contrib/taxize_0.9.98.tar.gz
Source0  : https://cran.r-project.org/src/contrib/taxize_0.9.98.tar.gz
Summary  : Taxonomic Information from Around the Web
Group    : Development/Tools
License  : MIT
Requires: R-R6
Requires: R-ape
Requires: R-bold
Requires: R-cli
Requires: R-conditionz
Requires: R-crayon
Requires: R-crul
Requires: R-data.table
Requires: R-foreach
Requires: R-jsonlite
Requires: R-natserv
Requires: R-phangorn
Requires: R-ritis
Requires: R-rotl
Requires: R-rredlist
Requires: R-tibble
Requires: R-wikitaxa
Requires: R-worrms
Requires: R-xml2
Requires: R-zoo
BuildRequires : R-R6
BuildRequires : R-ape
BuildRequires : R-bold
BuildRequires : R-cli
BuildRequires : R-conditionz
BuildRequires : R-crayon
BuildRequires : R-crul
BuildRequires : R-data.table
BuildRequires : R-foreach
BuildRequires : R-jsonlite
BuildRequires : R-natserv
BuildRequires : R-phangorn
BuildRequires : R-ritis
BuildRequires : R-rotl
BuildRequires : R-rredlist
BuildRequires : R-tibble
BuildRequires : R-wikitaxa
BuildRequires : R-worrms
BuildRequires : R-xml2
BuildRequires : R-zoo
BuildRequires : buildreq-R

%description
such as getting database specific taxonomic identifiers, verifying
    species names, getting taxonomic hierarchies, fetching downstream and
    upstream taxonomic names, getting taxonomic synonyms, converting
    scientific to common names and vice versa, and more.

%prep
%setup -q -c -n taxize
cd %{_builddir}/taxize

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603386572

%install
export SOURCE_DATE_EPOCH=1603386572
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library taxize
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library taxize
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library taxize
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc taxize || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/taxize/CITATION
/usr/lib64/R/library/taxize/DESCRIPTION
/usr/lib64/R/library/taxize/INDEX
/usr/lib64/R/library/taxize/LICENSE
/usr/lib64/R/library/taxize/Meta/Rd.rds
/usr/lib64/R/library/taxize/Meta/data.rds
/usr/lib64/R/library/taxize/Meta/features.rds
/usr/lib64/R/library/taxize/Meta/hsearch.rds
/usr/lib64/R/library/taxize/Meta/links.rds
/usr/lib64/R/library/taxize/Meta/nsInfo.rds
/usr/lib64/R/library/taxize/Meta/package.rds
/usr/lib64/R/library/taxize/Meta/vignette.rds
/usr/lib64/R/library/taxize/NAMESPACE
/usr/lib64/R/library/taxize/NEWS.md
/usr/lib64/R/library/taxize/R/taxize
/usr/lib64/R/library/taxize/R/taxize.rdb
/usr/lib64/R/library/taxize/R/taxize.rdx
/usr/lib64/R/library/taxize/data/Rdata.rdb
/usr/lib64/R/library/taxize/data/Rdata.rds
/usr/lib64/R/library/taxize/data/Rdata.rdx
/usr/lib64/R/library/taxize/doc/case_study.Rmd
/usr/lib64/R/library/taxize/doc/case_study.html
/usr/lib64/R/library/taxize/doc/index.html
/usr/lib64/R/library/taxize/doc/infotable.Rmd
/usr/lib64/R/library/taxize/doc/infotable.html
/usr/lib64/R/library/taxize/doc/name_cleaning.Rmd
/usr/lib64/R/library/taxize/doc/name_cleaning.html
/usr/lib64/R/library/taxize/doc/taxize.Rmd
/usr/lib64/R/library/taxize/doc/taxize.html
/usr/lib64/R/library/taxize/examples/species.txt
/usr/lib64/R/library/taxize/help/AnIndex
/usr/lib64/R/library/taxize/help/aliases.rds
/usr/lib64/R/library/taxize/help/figures/screencast.png
/usr/lib64/R/library/taxize/help/paths.rds
/usr/lib64/R/library/taxize/help/taxize.rdb
/usr/lib64/R/library/taxize/help/taxize.rdx
/usr/lib64/R/library/taxize/html/00Index.html
/usr/lib64/R/library/taxize/html/R.css
/usr/lib64/R/library/taxize/ignore/aou_notes.R
/usr/lib64/R/library/taxize/ignore/apg_script.R
/usr/lib64/R/library/taxize/ignore/nature_serve.R
/usr/lib64/R/library/taxize/ignore/phylomatic_tree2.R
/usr/lib64/R/library/taxize/ignore/phytools_fxns_touse.r
/usr/lib64/R/library/taxize/ignore/rank_ref_script.R
/usr/lib64/R/library/taxize/ignore/rbladj.r
/usr/lib64/R/library/taxize/ignore/taxonclass.R
/usr/lib64/R/library/taxize/ignore/taxonclass2.R
/usr/lib64/R/library/taxize/ignore/taxonid.R
/usr/lib64/R/library/taxize/ignore/tests/test-ubio_classification.R
/usr/lib64/R/library/taxize/ignore/tests/test-ubio_id.R
/usr/lib64/R/library/taxize/ignore/tests/test-ubio_namebank.R
/usr/lib64/R/library/taxize/ignore/tests/test-ubio_search.R
/usr/lib64/R/library/taxize/ignore/tests/test-ubio_synonyms.R
/usr/lib64/R/library/taxize/ignore/try_with_timeout.R
/usr/lib64/R/library/taxize/tests/fixtures/apgFamilies.yml
/usr/lib64/R/library/taxize/tests/fixtures/apgOrders.yml
/usr/lib64/R/library/taxize/tests/fixtures/bold_children.yml
/usr/lib64/R/library/taxize/tests/fixtures/bold_children_no_results.yml
/usr/lib64/R/library/taxize/tests/fixtures/bold_downstream.yml
/usr/lib64/R/library/taxize/tests/fixtures/bold_downstream_intermediate.yml
/usr/lib64/R/library/taxize/tests/fixtures/bold_ping.yml
/usr/lib64/R/library/taxize/tests/fixtures/bold_search.yml
/usr/lib64/R/library/taxize/tests/fixtures/children_ambiguous_ncbi.yml
/usr/lib64/R/library/taxize/tests/fixtures/children_bold.yml
/usr/lib64/R/library/taxize/tests/fixtures/children_itis_types.yml
/usr/lib64/R/library/taxize/tests/fixtures/children_no_results.yml
/usr/lib64/R/library/taxize/tests/fixtures/children_no_results_structure_ncbi_x.yml
/usr/lib64/R/library/taxize/tests/fixtures/children_no_results_structure_ncbi_y.yml
/usr/lib64/R/library/taxize/tests/fixtures/children_no_results_structure_x.yml
/usr/lib64/R/library/taxize/tests/fixtures/children_no_results_structure_y.yml
/usr/lib64/R/library/taxize/tests/fixtures/children_rows_param.yml
/usr/lib64/R/library/taxize/tests/fixtures/children_warn_on_db_mismatch.yml
/usr/lib64/R/library/taxize/tests/fixtures/children_with_id.yml
/usr/lib64/R/library/taxize/tests/fixtures/children_with_name.yml
/usr/lib64/R/library/taxize/tests/fixtures/class2tree_classification_call.yml
/usr/lib64/R/library/taxize/tests/fixtures/class2tree_classification_dup_call.yml
/usr/lib64/R/library/taxize/tests/fixtures/class2tree_internal_fxns.yml
/usr/lib64/R/library/taxize/tests/fixtures/classification.yml
/usr/lib64/R/library/taxize/tests/fixtures/classification_cbind_rbind.yml
/usr/lib64/R/library/taxize/tests/fixtures/classification_fetches_merged_taxon.yml
/usr/lib64/R/library/taxize/tests/fixtures/classification_gbif.yml
/usr/lib64/R/library/taxize/tests/fixtures/classification_gbif_get_fxn.yml
/usr/lib64/R/library/taxize/tests/fixtures/classification_gbif_ranks_below_species_subsp.yml
/usr/lib64/R/library/taxize/tests/fixtures/classification_gbif_ranks_below_species_var.yml
/usr/lib64/R/library/taxize/tests/fixtures/classification_gbif_ranks_correct_order.yml
/usr/lib64/R/library/taxize/tests/fixtures/classification_get_fxn.yml
/usr/lib64/R/library/taxize/tests/fixtures/classification_no_results.yml
/usr/lib64/R/library/taxize/tests/fixtures/classification_passing_id.yml
/usr/lib64/R/library/taxize/tests/fixtures/classification_pow.yml
/usr/lib64/R/library/taxize/tests/fixtures/classification_pow_cbind_rbind.yml
/usr/lib64/R/library/taxize/tests/fixtures/classification_pow_get_fxn.yml
/usr/lib64/R/library/taxize/tests/fixtures/classification_pow_more_name_egs.yml
/usr/lib64/R/library/taxize/tests/fixtures/classification_pow_no_results.yml
/usr/lib64/R/library/taxize/tests/fixtures/classification_pow_passing_id.yml
/usr/lib64/R/library/taxize/tests/fixtures/classification_rank_is_lowercase.yml
/usr/lib64/R/library/taxize/tests/fixtures/classification_rows_param.yml
/usr/lib64/R/library/taxize/tests/fixtures/classification_variety_of_names.yml
/usr/lib64/R/library/taxize/tests/fixtures/classification_warn_on_db_mismatch.yml
/usr/lib64/R/library/taxize/tests/fixtures/comm2sci.yml
/usr/lib64/R/library/taxize/tests/fixtures/comm2sci_warn_on_db_mismatch.yml
/usr/lib64/R/library/taxize/tests/fixtures/downstream.yml
/usr/lib64/R/library/taxize/tests/fixtures/downstream_bold.yml
/usr/lib64/R/library/taxize/tests/fixtures/downstream_id_input.yml
/usr/lib64/R/library/taxize/tests/fixtures/downstream_multiple_data_sources.yml
/usr/lib64/R/library/taxize/tests/fixtures/downstream_rows_param.yml
/usr/lib64/R/library/taxize/tests/fixtures/downstream_warn_on_db_mismatch.yml
/usr/lib64/R/library/taxize/tests/fixtures/eol_dataobjects.yml
/usr/lib64/R/library/taxize/tests/fixtures/eol_dataobjects_taxonomy_param.yml
/usr/lib64/R/library/taxize/tests/fixtures/eol_pages.yml
/usr/lib64/R/library/taxize/tests/fixtures/eol_pages2.yml
/usr/lib64/R/library/taxize/tests/fixtures/eol_search.yml
/usr/lib64/R/library/taxize/tests/fixtures/eubon_search.yml
/usr/lib64/R/library/taxize/tests/fixtures/fg_author_search.yml
/usr/lib64/R/library/taxize/tests/fixtures/fg_epithet_search.yml
/usr/lib64/R/library/taxize/tests/fixtures/fg_name_by_key.yml
/usr/lib64/R/library/taxize/tests/fixtures/fg_name_full_by_lsid.yml
/usr/lib64/R/library/taxize/tests/fixtures/fg_name_search.yml
/usr/lib64/R/library/taxize/tests/fixtures/gbif_downstream.yml
/usr/lib64/R/library/taxize/tests/fixtures/gbif_downstream_intermediate.yml
/usr/lib64/R/library/taxize/tests/fixtures/gbif_downstream_pagination.yml
/usr/lib64/R/library/taxize/tests/fixtures/gbif_parse.yml
/usr/lib64/R/library/taxize/tests/fixtures/gbif_ping.yml
/usr/lib64/R/library/taxize/tests/fixtures/genbank2uid.yml
/usr/lib64/R/library/taxize/tests/fixtures/genbank2uid_fails.yml
/usr/lib64/R/library/taxize/tests/fixtures/genbank2uid_gi_numbers.yml
/usr/lib64/R/library/taxize/tests/fixtures/get_boldid.yml
/usr/lib64/R/library/taxize/tests/fixtures/get_boldid_ask_false.yml
/usr/lib64/R/library/taxize/tests/fixtures/get_boldid_no_parent_name.yml
/usr/lib64/R/library/taxize/tests/fixtures/get_colid.yml
/usr/lib64/R/library/taxize/tests/fixtures/get_colid_ask_arg.yml
/usr/lib64/R/library/taxize/tests/fixtures/get_eolid.yml
/usr/lib64/R/library/taxize/tests/fixtures/get_eolid_ask_param.yml
/usr/lib64/R/library/taxize/tests/fixtures/get_gbifid.yml
/usr/lib64/R/library/taxize/tests/fixtures/get_gbifid_ask_arg.yml
/usr/lib64/R/library/taxize/tests/fixtures/get_gbifid_class_doesnt_matter.yml
/usr/lib64/R/library/taxize/tests/fixtures/get_gbifid_method_param.yml
/usr/lib64/R/library/taxize/tests/fixtures/get_gbifid_phylum_param.yml
/usr/lib64/R/library/taxize/tests/fixtures/get_gbifid_state.yml
/usr/lib64/R/library/taxize/tests/fixtures/get_natservid.yml
/usr/lib64/R/library/taxize/tests/fixtures/get_natservid_ask_arg.yml
/usr/lib64/R/library/taxize/tests/fixtures/get_pow.yml
/usr/lib64/R/library/taxize/tests/fixtures/get_pow_ask_arg.yml
/usr/lib64/R/library/taxize/tests/fixtures/get_tolid.yml
/usr/lib64/R/library/taxize/tests/fixtures/get_tolid_ask_arg.yml
/usr/lib64/R/library/taxize/tests/fixtures/get_tpsid.yml
/usr/lib64/R/library/taxize/tests/fixtures/get_tpsid_ask_arg.yml
/usr/lib64/R/library/taxize/tests/fixtures/get_tpsid_warnings_dots.yml
/usr/lib64/R/library/taxize/tests/fixtures/get_tpsid_warnings_subspecific.yml
/usr/lib64/R/library/taxize/tests/fixtures/get_tsn.yml
/usr/lib64/R/library/taxize/tests/fixtures/get_tsn_ask_verbose_args.yml
/usr/lib64/R/library/taxize/tests/fixtures/get_uid.yml
/usr/lib64/R/library/taxize/tests/fixtures/get_uid_ask_arg.yml
/usr/lib64/R/library/taxize/tests/fixtures/get_uid_filtering_division.yml
/usr/lib64/R/library/taxize/tests/fixtures/get_uid_filtering_rank.yml
/usr/lib64/R/library/taxize/tests/fixtures/get_uid_name_modifiers.yml
/usr/lib64/R/library/taxize/tests/fixtures/get_uid_rank_modifiers.yml
/usr/lib64/R/library/taxize/tests/fixtures/get_wormsid.yml
/usr/lib64/R/library/taxize/tests/fixtures/get_wormsid_ask_arg.yml
/usr/lib64/R/library/taxize/tests/fixtures/get_wormsid_fail_with_rows_unknown.yml
/usr/lib64/R/library/taxize/tests/fixtures/get_wormsid_fuzzy.yml
/usr/lib64/R/library/taxize/tests/fixtures/get_wormsid_marine_only.yml
/usr/lib64/R/library/taxize/tests/fixtures/get_wormsid_multiple_exact_matches_found.yml
/usr/lib64/R/library/taxize/tests/fixtures/get_wormsid_query_modifiers.yml
/usr/lib64/R/library/taxize/tests/fixtures/gn_parse.yml
/usr/lib64/R/library/taxize/tests/fixtures/gni_details.yml
/usr/lib64/R/library/taxize/tests/fixtures/gni_parse.yml
/usr/lib64/R/library/taxize/tests/fixtures/gni_search.yml
/usr/lib64/R/library/taxize/tests/fixtures/gnr_datasources.yml
/usr/lib64/R/library/taxize/tests/fixtures/id2name_warn_on_db_mismatch.yml
/usr/lib64/R/library/taxize/tests/fixtures/ion.yml
/usr/lib64/R/library/taxize/tests/fixtures/ion_fails_well.yml
/usr/lib64/R/library/taxize/tests/fixtures/ipni_search.yml
/usr/lib64/R/library/taxize/tests/fixtures/ipni_search_no_results.yml
/usr/lib64/R/library/taxize/tests/fixtures/ipni_search_output_formats.yml
/usr/lib64/R/library/taxize/tests/fixtures/itis_acceptname.yml
/usr/lib64/R/library/taxize/tests/fixtures/itis_acceptname_non_accepted_tsn.yml
/usr/lib64/R/library/taxize/tests/fixtures/itis_downstream.yml
/usr/lib64/R/library/taxize/tests/fixtures/itis_getrecord.yml
/usr/lib64/R/library/taxize/tests/fixtures/itis_hierarchy.yml
/usr/lib64/R/library/taxize/tests/fixtures/itis_kingdomnames.yml
/usr/lib64/R/library/taxize/tests/fixtures/itis_kingdomnames_fail_well.yml
/usr/lib64/R/library/taxize/tests/fixtures/itis_kingdomnames_with_tsns.yml
/usr/lib64/R/library/taxize/tests/fixtures/itis_lsid.yml
/usr/lib64/R/library/taxize/tests/fixtures/itis_native.yml
/usr/lib64/R/library/taxize/tests/fixtures/itis_ping.yml
/usr/lib64/R/library/taxize/tests/fixtures/itis_ping_http_code_200.yml
/usr/lib64/R/library/taxize/tests/fixtures/itis_ping_http_code_503.yml
/usr/lib64/R/library/taxize/tests/fixtures/itis_refs.yml
/usr/lib64/R/library/taxize/tests/fixtures/itis_taxrank.yml
/usr/lib64/R/library/taxize/tests/fixtures/itis_terms.yml
/usr/lib64/R/library/taxize/tests/fixtures/iucn_getname.yml
/usr/lib64/R/library/taxize/tests/fixtures/iucn_id.yml
/usr/lib64/R/library/taxize/tests/fixtures/iucn_id_fail.yml
/usr/lib64/R/library/taxize/tests/fixtures/iucn_summary.yml
/usr/lib64/R/library/taxize/tests/fixtures/iucn_summary_other_egs.yml
/usr/lib64/R/library/taxize/tests/fixtures/nbn_ping.yml
/usr/lib64/R/library/taxize/tests/fixtures/ncbi_children.yml
/usr/lib64/R/library/taxize/tests/fixtures/ncbi_children_ambiguous.yml
/usr/lib64/R/library/taxize/tests/fixtures/ncbi_children_id_class_check.yml
/usr/lib64/R/library/taxize/tests/fixtures/ncbi_downstream.yml
/usr/lib64/R/library/taxize/tests/fixtures/ncbi_downstream_ambiguous_false.yml
/usr/lib64/R/library/taxize/tests/fixtures/ncbi_downstream_ambiguous_true.yml
/usr/lib64/R/library/taxize/tests/fixtures/ncbi_downstream_handles_self_ids.yml
/usr/lib64/R/library/taxize/tests/fixtures/ncbi_get_taxon_summary.yml
/usr/lib64/R/library/taxize/tests/fixtures/ncbi_get_taxon_summary_many_ids_long.yml
/usr/lib64/R/library/taxize/tests/fixtures/ncbi_get_taxon_summary_many_ids_short.yml
/usr/lib64/R/library/taxize/tests/fixtures/ncbi_ping.yml
/usr/lib64/R/library/taxize/tests/fixtures/plantminer.yml
/usr/lib64/R/library/taxize/tests/fixtures/plantminer_not_found.yml
/usr/lib64/R/library/taxize/tests/fixtures/pow_lookup.yml
/usr/lib64/R/library/taxize/tests/fixtures/pow_lookup_include_param.yml
/usr/lib64/R/library/taxize/tests/fixtures/pow_search.yml
/usr/lib64/R/library/taxize/tests/fixtures/sci2comm.yml
/usr/lib64/R/library/taxize/tests/fixtures/sci2comm_warn_on_db_mismatch.yml
/usr/lib64/R/library/taxize/tests/fixtures/synonyms_itis.yml
/usr/lib64/R/library/taxize/tests/fixtures/synonyms_name_found_but_no_synonyms.yml
/usr/lib64/R/library/taxize/tests/fixtures/synonyms_name_not_found.yml
/usr/lib64/R/library/taxize/tests/fixtures/synonyms_warn_on_db_mismatch.yml
/usr/lib64/R/library/taxize/tests/fixtures/synonyms_worms.yml
/usr/lib64/R/library/taxize/tests/fixtures/tax_name_arg_arg.yml
/usr/lib64/R/library/taxize/tests/fixtures/tax_name_itis.yml
/usr/lib64/R/library/taxize/tests/fixtures/tax_name_na.yml
/usr/lib64/R/library/taxize/tests/fixtures/tax_name_ncbi.yml
/usr/lib64/R/library/taxize/tests/fixtures/tax_name_no_data.yml
/usr/lib64/R/library/taxize/tests/fixtures/tax_name_rows_Arg.yml
/usr/lib64/R/library/taxize/tests/fixtures/tax_name_throws_warning.yml
/usr/lib64/R/library/taxize/tests/fixtures/tax_rank.yml
/usr/lib64/R/library/taxize/tests/fixtures/tax_rank_get_star_input.yml
/usr/lib64/R/library/taxize/tests/fixtures/taxon_state_get_gbifid.yml
/usr/lib64/R/library/taxize/tests/fixtures/taxon_state_get_uid.yml
/usr/lib64/R/library/taxize/tests/fixtures/tnrs.yml
/usr/lib64/R/library/taxize/tests/fixtures/tnrs_order_row_names.yml
/usr/lib64/R/library/taxize/tests/fixtures/tnrs_sources.yml
/usr/lib64/R/library/taxize/tests/fixtures/tol_resolve.yml
/usr/lib64/R/library/taxize/tests/fixtures/tol_resolve_context_name.yml
/usr/lib64/R/library/taxize/tests/fixtures/tol_resolve_do_approximate_matching.yml
/usr/lib64/R/library/taxize/tests/fixtures/tol_resolve_do_approximate_matching_false.yml
/usr/lib64/R/library/taxize/tests/fixtures/tp_accnames.yml
/usr/lib64/R/library/taxize/tests/fixtures/tp_dist.yml
/usr/lib64/R/library/taxize/tests/fixtures/tp_refs.yml
/usr/lib64/R/library/taxize/tests/fixtures/tp_search.yml
/usr/lib64/R/library/taxize/tests/fixtures/tp_search_warnings_dots.yml
/usr/lib64/R/library/taxize/tests/fixtures/tp_search_warnings_subspecific.yml
/usr/lib64/R/library/taxize/tests/fixtures/tp_summary.yml
/usr/lib64/R/library/taxize/tests/fixtures/tp_synonyms.yml
/usr/lib64/R/library/taxize/tests/fixtures/trpicos_ping.yml
/usr/lib64/R/library/taxize/tests/fixtures/upstream.yml
/usr/lib64/R/library/taxize/tests/fixtures/vascan_ping.yml
/usr/lib64/R/library/taxize/tests/fixtures/vascan_search.yml
/usr/lib64/R/library/taxize/tests/fixtures/worms_downstream.yml
/usr/lib64/R/library/taxize/tests/fixtures/worms_downstream_intermediate_param.yml
/usr/lib64/R/library/taxize/tests/fixtures/worms_downstream_previously_unaccounted_for_ranks.yml
/usr/lib64/R/library/taxize/tests/fixtures/worms_downstream_start_param.yml
/usr/lib64/R/library/taxize/tests/test-all.R
/usr/lib64/R/library/taxize/tests/testthat/Rplots.pdf
/usr/lib64/R/library/taxize/tests/testthat/helper-taxize.R
/usr/lib64/R/library/taxize/tests/testthat/test-apgscraping.R
/usr/lib64/R/library/taxize/tests/testthat/test-bold_children.R
/usr/lib64/R/library/taxize/tests/testthat/test-bold_downstream.R
/usr/lib64/R/library/taxize/tests/testthat/test-bold_search.R
/usr/lib64/R/library/taxize/tests/testthat/test-children.R
/usr/lib64/R/library/taxize/tests/testthat/test-class2tree.R
/usr/lib64/R/library/taxize/tests/testthat/test-classification-gbif.R
/usr/lib64/R/library/taxize/tests/testthat/test-classification-pow.R
/usr/lib64/R/library/taxize/tests/testthat/test-classification.R
/usr/lib64/R/library/taxize/tests/testthat/test-comm2sci.R
/usr/lib64/R/library/taxize/tests/testthat/test-dataset_rank_ref.R
/usr/lib64/R/library/taxize/tests/testthat/test-downstream.R
/usr/lib64/R/library/taxize/tests/testthat/test-eol_dataobjects.R
/usr/lib64/R/library/taxize/tests/testthat/test-eol_pages.R
/usr/lib64/R/library/taxize/tests/testthat/test-eol_ping.R
/usr/lib64/R/library/taxize/tests/testthat/test-eol_search.R
/usr/lib64/R/library/taxize/tests/testthat/test-eubon.R
/usr/lib64/R/library/taxize/tests/testthat/test-fungorum.R
/usr/lib64/R/library/taxize/tests/testthat/test-gbif_downstream.R
/usr/lib64/R/library/taxize/tests/testthat/test-gbif_parse.R
/usr/lib64/R/library/taxize/tests/testthat/test-genbank2uid.R
/usr/lib64/R/library/taxize/tests/testthat/test-get_boldid.R
/usr/lib64/R/library/taxize/tests/testthat/test-get_eolid.R
/usr/lib64/R/library/taxize/tests/testthat/test-get_gbifid.R
/usr/lib64/R/library/taxize/tests/testthat/test-get_ids.R
/usr/lib64/R/library/taxize/tests/testthat/test-get_natservid.R
/usr/lib64/R/library/taxize/tests/testthat/test-get_pow.R
/usr/lib64/R/library/taxize/tests/testthat/test-get_tolid.R
/usr/lib64/R/library/taxize/tests/testthat/test-get_tpsid.R
/usr/lib64/R/library/taxize/tests/testthat/test-get_tsn.R
/usr/lib64/R/library/taxize/tests/testthat/test-get_uid.R
/usr/lib64/R/library/taxize/tests/testthat/test-get_wormsid.R
/usr/lib64/R/library/taxize/tests/testthat/test-gn_parse.R
/usr/lib64/R/library/taxize/tests/testthat/test-gni_details.R
/usr/lib64/R/library/taxize/tests/testthat/test-gni_parse.R
/usr/lib64/R/library/taxize/tests/testthat/test-gni_search.R
/usr/lib64/R/library/taxize/tests/testthat/test-gnr_datasources.R
/usr/lib64/R/library/taxize/tests/testthat/test-gnr_resolve.R
/usr/lib64/R/library/taxize/tests/testthat/test-id2name.R
/usr/lib64/R/library/taxize/tests/testthat/test-ion.R
/usr/lib64/R/library/taxize/tests/testthat/test-ipni_search.R
/usr/lib64/R/library/taxize/tests/testthat/test-itis_acceptname.R
/usr/lib64/R/library/taxize/tests/testthat/test-itis_downstream.R
/usr/lib64/R/library/taxize/tests/testthat/test-itis_getrecord.R
/usr/lib64/R/library/taxize/tests/testthat/test-itis_hierarchy.R
/usr/lib64/R/library/taxize/tests/testthat/test-itis_kingdomnames.R
/usr/lib64/R/library/taxize/tests/testthat/test-itis_lsid.R
/usr/lib64/R/library/taxize/tests/testthat/test-itis_native.R
/usr/lib64/R/library/taxize/tests/testthat/test-itis_ping.R
/usr/lib64/R/library/taxize/tests/testthat/test-itis_refs.R
/usr/lib64/R/library/taxize/tests/testthat/test-itis_taxrank.R
/usr/lib64/R/library/taxize/tests/testthat/test-itis_terms.R
/usr/lib64/R/library/taxize/tests/testthat/test-iucn_getname.R
/usr/lib64/R/library/taxize/tests/testthat/test-iucn_id.R
/usr/lib64/R/library/taxize/tests/testthat/test-iucn_summary.R
/usr/lib64/R/library/taxize/tests/testthat/test-key_helpers.R
/usr/lib64/R/library/taxize/tests/testthat/test-lowest_common.R
/usr/lib64/R/library/taxize/tests/testthat/test-names_list.R
/usr/lib64/R/library/taxize/tests/testthat/test-ncbi_children.R
/usr/lib64/R/library/taxize/tests/testthat/test-ncbi_downstream.R
/usr/lib64/R/library/taxize/tests/testthat/test-ncbi_get_taxon_summary.R
/usr/lib64/R/library/taxize/tests/testthat/test-ping.R
/usr/lib64/R/library/taxize/tests/testthat/test-plantminer.R
/usr/lib64/R/library/taxize/tests/testthat/test-pow_search.R
/usr/lib64/R/library/taxize/tests/testthat/test-progressor.R
/usr/lib64/R/library/taxize/tests/testthat/test-rankagg.R
/usr/lib64/R/library/taxize/tests/testthat/test-sci2comm.R
/usr/lib64/R/library/taxize/tests/testthat/test-synonyms.R
/usr/lib64/R/library/taxize/tests/testthat/test-tax_agg.R
/usr/lib64/R/library/taxize/tests/testthat/test-tax_name.R
/usr/lib64/R/library/taxize/tests/testthat/test-tax_rank.R
/usr/lib64/R/library/taxize/tests/testthat/test-taxon_state.R
/usr/lib64/R/library/taxize/tests/testthat/test-tnrs.R
/usr/lib64/R/library/taxize/tests/testthat/test-tnrs_sources.R
/usr/lib64/R/library/taxize/tests/testthat/test-tol_resolve.R
/usr/lib64/R/library/taxize/tests/testthat/test-tp_accnames.R
/usr/lib64/R/library/taxize/tests/testthat/test-tp_dist.R
/usr/lib64/R/library/taxize/tests/testthat/test-tp_refs.R
/usr/lib64/R/library/taxize/tests/testthat/test-tp_search.R
/usr/lib64/R/library/taxize/tests/testthat/test-tp_summary.R
/usr/lib64/R/library/taxize/tests/testthat/test-tp_synonyms.R
/usr/lib64/R/library/taxize/tests/testthat/test-upstream.R
/usr/lib64/R/library/taxize/tests/testthat/test-utils.R
/usr/lib64/R/library/taxize/tests/testthat/test-vascan_search.r
/usr/lib64/R/library/taxize/tests/testthat/test-worms_downstream.R
